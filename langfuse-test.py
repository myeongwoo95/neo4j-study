from langfuse import Langfuse
from dotenv import load_dotenv
import os

load_dotenv()

# Langfuse 연결 설정
langfuse_secret_key = os.getenv("LANGFUSE_SECRET_KEY")
langfuse_public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
langfuse_host = os.getenv("LANGFUSE_HOST")

# Langfuse 객체 생성
langfuse = Langfuse(
    secret_key=langfuse_secret_key,
    public_key=langfuse_public_key,
    host=langfuse_host
)