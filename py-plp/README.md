# Chapter 3 - 트렌스포머 모델을 다루기 위한 허깅페이스 트랜스포머 라이브러리

* * *

## 3주차 목표

- 허깅페이스 모델 허브에서 코딩 테스트에 적합한 모델을 찾고 적용하기
- ~~Openai의 codex 사용하기~~ (Openai에서 지원하지 않음)

### ~~코드 생성 모델 리더보드~~

[링크](https://huggingface.co/spaces/mike-ravkine/can-ai-code-results)

### AI 코드 생성 모델 비교

코드 생성에 특화된 여러 AI 모델들에 대한 개요를 제공합니다. 각 모델은 기능과 강점이 다르며, 다양한 작업에 적합하게 설계되었습니다. **Codex (OpenAI)**, **StarCoder (Hugging
Face)**, **CodeT5 (Salesforce Research)**, **AlphaCode (DeepMind)**의 비교 내용은 아래 표에서 확인할 수 있습니다.

| 모델                               | 특징                                               | 강점                                                                                                         | 적합성                                          |
|----------------------------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| **Codex (OpenAI)**               | 자연어로 설명된 문제를 바탕으로 코드를 생성하는 GPT-3 기반의 코드 특화 버전.   | - 코드 자동 생성 및 설명이 우수함. <br> - 다양한 프로그래밍 언어 지원 (Python, Java, JavaScript 등). <br> - OpenAI API를 통해 쉽게 연동 가능. | 사용자 입력을 받아 자동으로 코드를 생성하는 기능 구현에 매우 적합.       |
| **StarCoder (Hugging Face)**     | 여러 프로그래밍 언어에 대한 풍부한 지식을 가진, 코드 생성에 특화된 대형 언어 모델. | - 오픈소스로 제공되어 커스터마이징 가능. <br> - 다양한 언어와 플랫폼을 지원. <br> - 활발한 커뮤니티 지원.                                        | 맞춤형 AI 솔루션 개발이 필요하거나, 다양한 커스터마이징이 필요할 때 적합.  |
| **CodeT5 (Salesforce Research)** | 코드 생성, 요약, 번역, 오류 수정과 같은 작업에 뛰어난 T5 모델의 변형.      | - 다양한 코드 관련 작업 수행 가능 (예: 오류 수정, 코드 변환). <br> - Hugging Face에서 쉽게 사용 가능.                                    | 코드 문제 해결 외에도 코드 리뷰, 개선 및 오류 해결 기능을 추가할 때 유용. |
| **AlphaCode (DeepMind)**         | 경쟁 프로그래밍 문제 해결에 특화된 모델로, 자연어 문제를 바탕으로 코드를 생성함.   | - 경쟁 프로그래밍 문제 해결에 탁월. <br> - 실제 코딩 대회에서 성능이 검증됨.                                                           | 코딩 테스트 문제 해결과 같은 기능을 목표로 할 때 매우 적합한 모델.      |

사용할 모델은 **StarCoder**입니다. api로 호출하는 방법과 fine-tuning 방법 모두 사용해 보고자 합니다.

### ~~한국어 코드 데이터셋~~

1. [Korea University Programming Dataset](https://huggingface.co/datasets/team-monolith/korea-university-programming-dataset):
   이 데이터셋은 2024년 고려대학교 프로그래밍 수업에서 수집된 학생들의 코딩 실행, 제출 내역, 문제 메타데이터 등을 포함하고 있습니다. 또한, 문제 해결 과정과 관련된 다양한 정보를 제공하여 교육 및 연구
   목적으로 활용될 수 있습니다.
    - 사용 허가 못 받음 (24/9/30)

* * *

## App 설명

### 주요 파일

- `app.py`: FastAPI 서버의 메인 엔트리 포인트. OpenAI 및 Hugging Face API 호출을 처리하는 REST 엔드포인트를 제공합니다.
- `services/openai_service.py`: OpenAI API를 호출하여 코드를 생성하는 서비스.
- `services/huggingface_service.py`: Hugging Face API를 호출하여 코드를 생성하는 서비스.
- `services/utils.py`: 프롬프트를 생성하는 유틸리티 함수가 정의된 파일.
- `models/request_model.py`: 요청 데이터의 유효성을 검사하는 Pydantic 모델 정의.
- `.env`: API 키를 안전하게 관리하기 위한 환경 변수 파일.

### API 엔드포인트

- URL:
    - OpenAI: `/generate-code/openai/`
    - Hugging Face: `/generate-code/huggingface/`
- Method: POST
- 요청 Body 예시:
  ```json
   {
  "prompt": "Write a Python function to reverse a string.",
  "example_inputs": ["'hello'"],
  "example_outputs": ["'olleh'"],
  "language": "Python",
  "max_tokens": 100 
   }
  ```
- 응답 예시:
   ```json
   {
     "generated_code": "def reverse_string(s):\n    return s[::-1]"
   }
   ```

### 설치 및 실행 방법

#### 1. 필수 패키지 설치

`requirements.txt` 파일을 사용하여 필요한 패키지를 설치할 수 있습니다:

```bash
pip install -r requirements.txt
```

#### 2. 환경 변수 설정

`.env` 파일에 OpenAI 및 Hugging Face API 키를 추가합니다:

```text
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

#### 3. 서버 실행

FastAPI 서버는 Uvicorn으로 실행합니다:

```bash
uvicorn app:app --reload
```

### 디렉토리 구조

```bash
my_project/
│
├── app.py                        # FastAPI 메인 파일
├── services/                     # 서비스 관련 파일
│   ├── __init__.py               # 패키지 인식 파일
│   ├── openai_service.py         # OpenAI API 서비스 파일
│   ├── huggingface_service.py    # Hugging Face API 서비스 파일
│   └── utils.py                  # 프롬프트 생성 유틸리티
├── models/                       # 데이터 모델 정의
│   └── request_model.py          # Pydantic 요청 모델 파일
└── .env                          # 환경 변수 파일
```