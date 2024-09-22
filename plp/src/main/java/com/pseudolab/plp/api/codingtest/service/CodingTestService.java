package com.pseudolab.plp.api.codingtest.service;

import com.pseudolab.plp.api.codingtest.dto.CodingTestRequestDto;

public interface CodingTestService {
    String generateCodingTestPrompt(CodingTestRequestDto request);

    String getCodingTestAnswer(String prompt);
}
