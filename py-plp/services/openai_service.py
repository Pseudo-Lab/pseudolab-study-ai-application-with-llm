import os

import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from services.utils import create_full_prompt

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 불러오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# OpenAI API 호출 함수 정의
def get_openai_completion(prompt: str, example_inputs: list, example_outputs: list, language: str, max_tokens: int):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    # 프롬프트 구성
    full_prompt = create_full_prompt(prompt, example_inputs, example_outputs, language)

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
