def create_full_prompt(prompt: str, example_inputs: list, example_outputs: list, language: str) -> str:
    """
    문제 설명과 예시 입력/출력을 바탕으로 프롬프트를 생성하는 함수.
    OpenAI 및 Hugging Face API에서 공통으로 사용.
    """
    full_prompt = (
        f"Generate {language} code based on the following problem:\n{prompt}\n"
        f"Example inputs: {example_inputs}\n"
        f"Example outputs: {example_outputs}\n"
    )
    return full_prompt
