# AGENTS.md

## 이 프로젝트에 대해
대학생 백엔드 스터디용 실시간 투표 앱. FastAPI + WebSocket.
팀원 3명 중 2명은 파이썬을 이번 학기에 처음 시작했다.

## 코드를 쓸 때 반드시 지킬 것
- **한국어 주석을 넉넉히 단다.** 무엇을 하는지가 아니라 왜 하는지를 쓴다.
- 파이썬 초보가 읽을 수 있는 수준으로 쓴다.
  쓰지 말 것: 복잡한 컴프리헨션 중첩, 메타클래스, 직접 만든 데코레이터, 과한 추상화
- 새 라이브러리를 추가하기 전에 먼저 물어본다.
- 파일 하나를 통째로 다시 쓰지 말고, 바꾼 부분만 최소한으로 수정한다.
- 코드를 만든 뒤에는 **핵심 개념 3줄 요약**을 같이 준다.

## 절대 하지 말 것
- `git push`, `git commit`, `git merge` 를 대신 실행하지 않는다. Git 명령은 사람이 직접 친다.
- main 브랜치에서 작업하지 않는다.
- `.env`, 비밀번호, API 키, DB 연결 문자열을 코드나 문서에 절대 넣지 않는다.
  **이 저장소는 public이다.**
- 요청하지 않은 파일을 건드리지 않는다.
- 테스트나 CI 설정을 임의로 바꾸지 않는다.

## 프로젝트 구조
    app/main.py          FastAPI 앱, 엔드포인트
    app/models.py        Pydantic / SQLModel 모델
    app/store.py         데이터 저장·조회
    app/db.py            DB 연결
    app/ws.py            WebSocket 연결 관리
    app/observability.py 요청 로그 미들웨어
    static/index.html    프론트엔드 (파일 하나로 유지)

## 명령어
    uv sync                                    의존성 설치
    uv run uvicorn app.main:app --reload       개발 서버
    uv export --no-hashes --format requirements-txt > requirements.txt
