import os
import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from typing import Dict, Any

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 불러오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# OpenAI API 호출 함수 정의
def get_chat_completion(prompt: str, max_tokens: int, additional_data: Dict[str, Any]):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    # 추가 데이터를 기반으로 전체 프롬프트 구성
    full_prompt = f"Prompt: {prompt}\n"

    # example_inputs와 example_outputs이 있다면 추가
    if 'example_inputs' in additional_data:
        full_prompt += f"Example inputs: {additional_data['example_inputs']}\n"
    if 'example_outputs' in additional_data:
        full_prompt += f"Example outputs: {additional_data['example_outputs']}\n"

    data = {
        "model": "gpt-3.5-turbo",  # 최신 모델 사용
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "max_tokens": max_tokens
    }

    # OpenAI API 호출
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Chat API 호출 오류: " + response.text)
