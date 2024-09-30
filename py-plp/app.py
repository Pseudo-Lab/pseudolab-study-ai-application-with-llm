from fastapi import FastAPI, HTTPException
from models.request_model import DynamicPromptRequest
from services.openai_service import get_chat_completion

# FastAPI 인스턴스 생성
app = FastAPI()

# 코드 생성 요청 엔드포인트
@app.post("/generate-code/")
async def generate_code(request: DynamicPromptRequest):
    try:
        # OpenAI 서비스 호출
        chat_response = get_chat_completion(
            request.prompt,
            request.max_tokens,
            {
                "example_inputs": request.example_inputs,
                "example_outputs": request.example_outputs,
                "language": request.language,
                "additional_data": request.additional_data
            }
        )
        # ChatGPT에서 반환된 코드 추출
        code_output = chat_response["choices"][0]["message"]["content"]
        return {"generated_code": code_output.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"코드 생성 중 오류 발생: {str(e)}")

# 기본 엔드포인트 확인
@app.get("/")
async def root():
    return {"message": "FastAPI 서버가 정상적으로 동작 중입니다."}
