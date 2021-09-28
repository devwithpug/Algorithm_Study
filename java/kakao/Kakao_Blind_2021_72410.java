// 2021 KAKAO BLIND RECRUITMENT 신규 아이디 추천 https://programmers.co.kr/learn/courses/30/lessons/72410

import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {

    private boolean isValid(String s) {
        char c = s.charAt(0);
        return Character.isLetter(c) || Character.isDigit(c)
                || c == '-' || c == '_' || c == '.';
    }

    public String solution(String new_id) {

        new_id = new_id.toLowerCase();
        String collect = Arrays.stream(new_id.split(""))
                .filter(this::isValid).collect(Collectors.joining());
        String result = "";
        for (String s : collect.split("\\.")) {
            if (!s.equals("")) {
                result += s + ".";
            }
        }
        if (result.endsWith(".")) result = result.substring(0, result.length() - 1);
        if (result.isEmpty()) result = "a";
        if (result.length() > 15) result = result.substring(0, 15);
        while (result.length() <= 2) result += result.substring(result.length() - 1);
        if (result.endsWith(".")) result = result.substring(0, result.length() - 1);

        return result;
    }
}