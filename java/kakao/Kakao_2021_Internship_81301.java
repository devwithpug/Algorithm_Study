// 2021 카카오 채용연계형 인턴십 - 숫자 문자열과 영단어
// https://programmers.co.kr/learn/courses/30/lessons/81301

import java.util.Map;

class Solution {
    public int solution(String s) {

        Map<String, String> map = Map.of(
                "zero", "0",
                "one", "1",
                "two", "2",
                "three", "3",
                "four", "4",
                "five", "5",
                "six", "6",
                "seven", "7",
                "eight", "8",
                "nine", "9"
        );

        String answer = "";
        String temp = "";

        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                answer += String.valueOf(s.charAt(i));
            } else {
                temp += String.valueOf(s.charAt(i));
                if (map.containsKey(temp)) {
                    answer += String.valueOf(map.get(temp));
                    temp = "";
                }
            }
        }

        return Integer.parseInt(answer);
    }
}