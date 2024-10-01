import os

import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from services.utils import create_full_prompt

# 환경 변수 로드
load_dotenv()

# Hugging Face API 토큰 불러오기
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


# Hugging Face API 호출 함수 정의
def get_huggingface_completion(prompt: str, example_inputs: list, example_outputs: list, language: str):
    API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder2-15b"
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    # 프롬프트 구성
    full_prompt = create_full_prompt(prompt, example_inputs, example_outputs, language)

    payload = {
        "inputs": full_prompt
    }

    # Hugging Face API 호출
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        response_json = response.json()

        # 응답이 리스트인지 확인 후 처리
        if isinstance(response_json, list):
            return response_json[0].get("generated_text", "No output generated")
        elif isinstance(response_json, dict):
            return response_json.get("generated_text", "No output generated")
        else:
            raise HTTPException(status_code=500, detail="알 수 없는 응답 형식")
    else:
        raise HTTPException(status_code=response.status_code, detail="Hugging Face API 호출 오류: " + response.text)
