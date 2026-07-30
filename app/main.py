"""LivePoll 웹 서버의 시작점(entry point).

이 파일 하나가 "서버 프로그램" 그 자체다.
uvicorn 이 이 파일을 읽어서 아래에 있는 `app` 이라는 변수를 찾아 실행한다.
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# ---------------------------------------------------------------------------
# 1. 폴더 위치 정해두기
# ---------------------------------------------------------------------------
# __file__ 은 "지금 이 파일(main.py)의 경로" 를 담고 있는 파이썬 기본 변수다.
#   .resolve()  -> 전체 경로로 바꾼다.  예) C:\Users\user\live-poll\app\main.py
#   .parent     -> 한 단계 위 폴더.     예) C:\Users\user\live-poll\app
#   .parent     -> 또 한 단계 위 폴더.  예) C:\Users\user\live-poll   <- 프로젝트 루트
BASE_DIR = Path(__file__).resolve().parent.parent

# 프로젝트 루트 아래의 static 폴더. HTML, CSS, 이미지 같은 파일을 넣는 곳이다.
# Path 끼리는 / 기호로 이어 붙일 수 있다. (윈도우/맥 상관없이 알아서 처리해 준다)
STATIC_DIR = BASE_DIR / "static"


# ---------------------------------------------------------------------------
# 2. FastAPI 앱 만들기
# ---------------------------------------------------------------------------
# 여기서 만든 app 객체에 "어떤 주소로 오면 무슨 일을 할지" 를 하나씩 등록해 나간다.
app = FastAPI(title="LivePoll", description="실시간 투표 서비스")


# ---------------------------------------------------------------------------
# 3. 엔드포인트(주소별 처리) 등록
# ---------------------------------------------------------------------------
# @app.get("...") 은 "이 주소로 GET 요청이 오면 바로 아래 함수를 실행해라" 라는 표시다.
# 이런 표시를 파이썬에서는 데코레이터(decorator)라고 부른다.


@app.get("/api/health")
def health_check():
    """서버가 살아있는지 확인하는 주소.

    브라우저에서 http://127.0.0.1:8000/api/health 로 들어가면
    {"status": "ok"} 라는 글자가 보인다.

    배포한 서버가 잘 떠 있는지 확인할 때 쓰고,
    Render 같은 배포 서비스도 이런 주소로 주기적으로 서버 상태를 확인한다.
    """
    # 파이썬 딕셔너리를 return 하면 FastAPI 가 알아서 JSON 으로 바꿔서 보내준다.
    return {"status": "ok"}


@app.get("/")
def index():
    """맨 앞 페이지(/)로 접속하면 static/index.html 파일을 그대로 보여준다.

    FileResponse 는 "파일 하나를 통째로 응답으로 보내라" 는 뜻이다.
    """
    return FileResponse(STATIC_DIR / "index.html")


# ---------------------------------------------------------------------------
# 4. static 폴더를 통째로 서빙하기
# ---------------------------------------------------------------------------
# 아래 한 줄 덕분에 static 폴더 안의 파일들을 /static/... 주소로 꺼내 쓸 수 있다.
#   static/style.css  ->  http://127.0.0.1:8000/static/style.css
#   static/logo.png   ->  http://127.0.0.1:8000/static/logo.png
# 나중에 CSS 나 JS 파일을 추가하면 index.html 에서 이 주소로 불러오면 된다.
#
# name="static" 은 이 마운트에 붙이는 이름표다. 지금 당장은 쓸 일이 없다.
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
