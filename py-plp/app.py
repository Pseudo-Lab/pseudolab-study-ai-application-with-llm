from fastapi import FastAPI, HTTPException
from models.request_model import CodeRequest
from services.openai_service import get_openai_completion
from services.huggingface_service import get_huggingface_completion

# FastAPI 인스턴스 생성
app = FastAPI()

# OpenAI API를 사용하는 엔드포인트
@app.post("/generate-code/openai/")
async def generate_code_openai(request: CodeRequest):
    try:
        # OpenAI 서비스 호출
        chat_response = get_openai_completion(
            request.prompt,
            request.example_inputs,
            request.example_outputs,
            request.language,
            request.max_tokens  # OpenAI는 max_tokens 필요
        )
        # ChatGPT에서 반환된 코드 추출
        code_output = chat_response["choices"][0]["message"]["content"]
        return {"generated_code": code_output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI 코드 생성 중 오류 발생: {str(e)}")

# Hugging Face API를 사용하는 엔드포인트
@app.post("/generate-code/huggingface/")
async def generate_code_huggingface(request: CodeRequest):
    try:
        # Hugging Face 서비스 호출
        code_output = get_huggingface_completion(
            request.prompt,
            request.example_inputs,
            request.example_outputs,
            request.language  # Hugging Face에서는 max_tokens 사용 안 함
        )
        return {"generated_code": code_output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hugging Face 코드 생성 중 오류 발생: {str(e)}")

# 기본 엔드포인트 확인
@app.get("/")
async def root():
    return {"message": "FastAPI 서버가 정상적으로 동작 중입니다."}
