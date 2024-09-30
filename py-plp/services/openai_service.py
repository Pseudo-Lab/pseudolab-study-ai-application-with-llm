import os
import requests
from dotenv import load_dotenv
from fastapi import HTTPException

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 불러오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# OpenAI API 호출 함수 정의
def get_chat_completion(prompt: str, max_tokens: int, example_inputs: list, example_outputs: list, language: str):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    # 전체 프롬프트 구성
    full_prompt = f"Prompt: {prompt}\n"
    if example_inputs:
        full_prompt += f"Example inputs: {example_inputs}\n"
    if example_outputs:
        full_prompt += f"Example outputs: {example_outputs}\n"

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "max_tokens": max_tokens
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="OpenAI API 호출 오류: " + response.text)
