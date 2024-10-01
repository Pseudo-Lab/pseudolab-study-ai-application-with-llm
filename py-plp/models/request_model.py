from pydantic import BaseModel
from typing import Optional, List, Any

# 요청 데이터 모델 정의
class CodeRequest(BaseModel):
    prompt: str  # 필수 필드
    example_inputs: Optional[List[Any]] = []  # 선택적 필드
    example_outputs: Optional[List[Any]] = []  # 선택적 필드
    language: Optional[str] = "Python"  # 기본값은 Python
    max_tokens: Optional[int] = 100  # 기본값은 100, hugging face에는 적용되지 않습니다.
