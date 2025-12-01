### uv 설정
```shell
# 프로젝트 초기화
uv init

# 가상환경 생성
uv venv .venv --python=3.12

# 가상환경 활성화 (window)
source .venv/Scripts/activate

# 가상환경 비활성화 (window)
deactivate
```

### .gitignore
.env 추가

### 파이썬 수정 
.python-version 파일에서 파이썬 버전 3.12으로 변경
pyproject.toml 파일에서 requires-python 필드 ">=3.11,<3.13" 으로 수정 
(의미: 3.12 이상 3.13미만)

### 패키지 설치
```shell
uv add python-dotenv langchain langchain-openai langchain-neo4j langchain-google-genai numpy ipykernel pandas langfuse langchain_experimental
```

### uv 명령어
```shell
uv run *.py
```