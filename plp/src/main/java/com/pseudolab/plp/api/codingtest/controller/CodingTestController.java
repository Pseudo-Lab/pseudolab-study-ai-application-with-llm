package com.pseudolab.plp.api.codingtest.controller;

import com.pseudolab.plp.api.codingtest.dto.CodingTestRequestDto;
import com.pseudolab.plp.api.codingtest.service.CodingTestService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class CodingTestController {

    private final CodingTestService codingTestService;

    @PostMapping("/algorithm/test")
    public String getCodingTestResponse(@RequestBody CodingTestRequestDto request) {
        // 코딩 테스트 관련 프롬프트 생성
        String prompt = codingTestService.generateCodingTestPrompt(request);
        // OpenAI로부터 결과를 받아옴
        return codingTestService.getCodingTestAnswer(prompt);
    }

}