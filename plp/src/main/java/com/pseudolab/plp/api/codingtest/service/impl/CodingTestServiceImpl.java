package com.pseudolab.plp.api.codingtest.service.impl;

import com.pseudolab.plp.api.codingtest.dto.CodingTestRequestDto;
import com.pseudolab.plp.api.codingtest.service.CodingTestService;
import lombok.RequiredArgsConstructor;
import org.springframework.ai.openai.OpenAiChatModel;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class CodingTestServiceImpl implements CodingTestService {

    private final OpenAiChatModel chatModel;

    @Override
    public String generateCodingTestPrompt(CodingTestRequestDto request) {
        StringBuilder prompt = new StringBuilder();

        // 문제 설명 추가
        prompt.append("You are solving a coding test. Below is the problem description:\n\n");
        prompt.append("Problem: ").append(request.getQuestion()).append("\n\n");

        // 예제 입력 및 출력 추가
        for (int i = 0; i < request.getExampleInputs().length; i++) {
            prompt.append("Example Input ").append(i + 1).append(": ").append(request.getExampleInputs()[i]).append("\n");
            prompt.append("Example Output ").append(i + 1).append(": ").append(request.getExampleOutputs()[i]).append("\n\n");
        }

        // 키워드 추가
        if (request.getKeywords() != null && request.getKeywords().length > 0) {
            prompt.append("Keywords: ").append(String.join(", ", request.getKeywords())).append("\n\n");
        }

        // 언어 추가
        prompt.append("Language: ").append(request.getLanguage().toString()).append("\n\n");

        // 사용자에게 답안을 생성해 달라는 요청
        prompt.append("Please provide a detailed solution in ").append(request.getLanguage().toString()).append(".");

        return prompt.toString();
    }

    @Override
    public String getCodingTestAnswer(String prompt) {
        return chatModel.call(prompt);
    }
}
