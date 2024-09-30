from pydantic import BaseModel
from typing import Optional, List, Dict, Any

# 요청 데이터 모델 정의 (프롬프트 형식이 유동적으로 변경 가능)
class DynamicPromptRequest(BaseModel):
    prompt: str  # 필수 프롬프트 필드
    max_tokens: Optional[int] = 100  # 기본값은 100, 선택적으로 조정 가능
    example_inputs: Optional[List[Any]] = []  # 예시 입력은 선택적
    example_outputs: Optional[List[Any]] = []  # 예시 출력은 선택적
    additional_data: Optional[Dict[str, Any]] = None  # 기타 동적 데이터 처리
    language: Optional[str] = "Python"  # 기본 언어는 Python
