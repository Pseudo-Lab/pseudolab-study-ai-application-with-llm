import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 불러오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# FastAPI 인스턴스 생성
app = FastAPI()

# 요청 데이터 모델 정의
class CodeRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

# OpenAI Chat Completion API 호출 함수
def get_chat_completion(prompt: str, max_tokens: int):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # 최신 모델로 변경 (gpt-3.5-turbo 또는 gpt-4)
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Chat API 호출 오류: " + response.text)

# 코드 생성 요청 엔드포인트
@app.post("/generate-code/")
async def generate_code(request: CodeRequest):
    try:
        # ChatGPT API 호출
        chat_response = get_chat_completion(request.prompt, request.max_tokens)
        # ChatGPT에서 반환된 코드 추출
        code_output = chat_response["choices"][0]["message"]["content"]
        return {"generated_code": code_output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"코드 생성 중 오류 발생: {str(e)}")

# 기본 엔드포인트 확인
@app.get("/")
async def root():
    return {"message": "FastAPI 서버가 정상적으로 동작 중입니다."}
