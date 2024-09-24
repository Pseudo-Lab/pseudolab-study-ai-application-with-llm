package com.pseudolab.plp.api.codingtest.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class CodingTestRequestDto {

    String question;
    String[] exampleInputs;
    String[] exampleOutputs;
    String[] keywords;
    Language language;

}
