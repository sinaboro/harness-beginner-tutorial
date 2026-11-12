# ============================================================
# Dockerfile - 0·1·2단계 공용 작업 환경
#
# 들어 있는 것: Python 3.12, pytest, Git, OpenCode(AI 에이전트), bash
# 파일은 Windows 폴더를 연결해서 쓴다(docker-compose.yml 참고).
# 그래서 이 이미지에는 교안의 예제나 학생 작업물을 넣지 않는다.
# ============================================================

FROM python:3.12-slim

# 파이썬이 쓸데없는 임시 파일(__pycache__)을 만들지 않게 하고, 출력이 바로 보이게 한다.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# 필요한 도구: bash(셸), git(기록), curl(OpenCode 내려받기), tar(압축 풀기), ripgrep(파일 찾기)
RUN apt-get update \
    && apt-get install -y --no-install-recommends bash ca-certificates curl git ripgrep tar \
    && rm -rf /var/lib/apt/lists/*

# 테스트 도구. 1단계부터 쓴다. 버전을 고정해서 수업 중에 바뀌지 않게 한다.
RUN pip install pytest==9.2.0

# AI 에이전트 OpenCode 설치. 버전을 고정한다. (교안은 2.x 기준)
ARG OPENCODE_VERSION=2.2.6
RUN curl -fsSL https://opencode.ai/v2/install | bash -s -- --version ${OPENCODE_VERSION} --no-modify-path
ENV PATH="/root/.opencode/bin:${PATH}"

# Git 설정
#  - safe.directory: Windows 에서 연결한 폴더를 Git 이 믿고 쓰게 한다. (수업용 컨테이너이므로 모든 폴더 허용)
#  - core.autocrlf input: 윈도우 줄바꿈(CRLF)이 저장소에 섞이지 않게 한다.
#  - core.fileMode false: 윈도우 폴더의 실행 권한 차이를 변경으로 보지 않게 한다.
RUN git config --system --add safe.directory '*' \
    && git config --system core.autocrlf input \
    && git config --system core.fileMode false \
    && git config --system init.defaultBranch main

# 작업 폴더. docker-compose.yml 이 여기에 Windows 의 C:\harness-lab 을 연결한다.
WORKDIR /workspace

CMD ["bash"]
