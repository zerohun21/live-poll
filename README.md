# LivePoll

실시간 투표 웹 서비스입니다.
발표나 수업 중에 질문을 올리면 참여자들이 바로 투표하고, 결과가 실시간으로 보이는 것을 목표로 합니다.

지금은 프로젝트 뼈대만 만들어 둔 상태입니다. (첫 화면 + 서버 상태 확인 API)

## 기술 스택

| 무엇 | 왜 쓰는지 |
| --- | --- |
| [Python](https://www.python.org/) 3.11+ | 서버를 만드는 프로그래밍 언어 |
| [FastAPI](https://fastapi.tiangolo.com/) | 웹 API 를 쉽게 만들어 주는 도구 |
| [uvicorn](https://www.uvicorn.org/) | 만든 앱을 실제로 실행해 주는 웹 서버 |
| [uv](https://docs.astral.sh/uv/) | 라이브러리 설치/관리 도구 (pip 보다 빠른 최신 도구) |

## 폴더 구조

```
live-poll/
├── app/                 # 서버 코드가 들어가는 곳
│   ├── __init__.py      # 이 폴더가 파이썬 패키지임을 알려주는 빈 파일
│   └── main.py          # 서버의 시작점. 주소별 처리를 여기에 적는다
├── static/              # 브라우저에 그대로 보내는 파일 (HTML, CSS, 이미지)
│   └── index.html       # 첫 화면
├── pyproject.toml       # 프로젝트 설정 + 필요한 라이브러리 목록
├── uv.lock              # 설치된 라이브러리의 정확한 버전 기록 (uv 가 자동 생성)
├── requirements.txt     # 배포용 라이브러리 목록 (uv.lock 에서 뽑아낸 것)
└── README.md            # 지금 읽고 있는 파일
```

## 로컬에서 실행하기

### 0. uv 설치 (처음 한 번만)

이미 깔려 있는지 먼저 확인해 보세요. 버전 번호가 나오면 설치된 것입니다.

```powershell
uv --version
```

없다면 아래 명령으로 설치합니다. ([공식 설치 문서](https://docs.astral.sh/uv/getting-started/installation/))

```powershell
# 윈도우 (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# 맥 / 리눅스
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 1. 코드 내려받기

```bash
git clone <이 저장소 주소>
cd live-poll
```

### 2. 라이브러리 설치

```bash
uv sync
```

이 명령 하나로 두 가지가 한 번에 됩니다.

1. `.venv` 라는 폴더를 만들어서 이 프로젝트 전용 파이썬 환경을 준비합니다.
   (다른 프로젝트와 라이브러리가 섞이지 않게 하려고 따로 만듭니다)
2. `pyproject.toml` 에 적힌 라이브러리들을 그 안에 설치합니다.

### 3. 서버 실행

```bash
uv run uvicorn app.main:app --reload
```

명령어를 뜯어보면 이런 뜻입니다.

- `uv run` : 방금 만든 `.venv` 환경 안에서 뒤에 오는 명령을 실행해라
- `uvicorn` : 웹 서버 실행 프로그램
- `app.main:app` : `app` 폴더의 `main.py` 파일 안에 있는 `app` 변수를 실행해라
- `--reload` : 코드를 고쳐서 저장하면 서버를 자동으로 다시 시작해라 (개발할 때만 씁니다)

### 4. 브라우저로 확인

서버가 뜨면 아래 주소들을 열어 보세요.

| 주소 | 보이는 것 |
| --- | --- |
| http://127.0.0.1:8000/ | "LivePoll 준비중" 첫 화면 |
| http://127.0.0.1:8000/api/health | `{"status":"ok"}` — 서버가 살아있다는 뜻 |
| http://127.0.0.1:8000/docs | FastAPI 가 자동으로 만들어 주는 API 문서 |

서버를 끌 때는 터미널에서 `Ctrl + C` 를 누릅니다.

## requirements.txt 만들기

Render 같은 배포 서비스는 아직 `uv` 를 기본으로 지원하지 않고 `requirements.txt` 파일을 봅니다.
그래서 `uv.lock` 의 내용을 `requirements.txt` 형식으로 뽑아내야 합니다.

```bash
uv export --no-hashes --no-dev --no-emit-project -o requirements.txt
```

옵션 뜻:

- `--no-hashes` : 파일 검증용 해시값을 빼서 파일을 짧고 읽기 쉽게 만든다
- `--no-dev` : 개발할 때만 쓰는 도구는 제외하고, 서버 실행에 꼭 필요한 것만 넣는다
- `--no-emit-project` : 우리 프로젝트 자신(`live-poll`)은 목록에서 뺀다
- `-o requirements.txt` : 결과를 이 파일로 저장한다

> **주의**
> 라이브러리를 새로 추가했다면 (`uv add ...`) 이 명령을 다시 실행해서
> `requirements.txt` 도 같이 갱신하고 커밋해야 합니다.
> 안 그러면 내 컴퓨터에서는 되는데 배포한 서버에서는 안 되는 일이 생깁니다.

## 배포

- **배포 URL**: (아직 배포 전 — 배포하고 나면 여기에 주소를 적어주세요)
- **배포 플랫폼**: [Render](https://render.com/)

Render 에서 새 Web Service 를 만들 때 아래 설정을 사용합니다.

| 항목 | 값 |
| --- | --- |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

로컬 실행 명령과 다른 부분:

- `--host 0.0.0.0` : 내 컴퓨터에서만이 아니라 바깥에서 들어오는 접속도 받는다
- `--port $PORT` : 포트 번호를 Render 가 정해서 알려주므로 그 값을 그대로 쓴다
- `--reload` 없음 : 배포 서버에서는 코드가 바뀔 일이 없으므로 뺀다
