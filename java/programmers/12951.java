// JadenCase 문자열 만들기 https://programmers.co.kr/learn/courses/30/lessons/12951

class Solution {
    public String solution(String s) {
        String answer = "";
        for (int i = 0; i < s.length(); i++) answer += i == 0 || s.charAt(i-1) == ' ' ? String.valueOf(s.charAt(i)).toUpperCase() : String.valueOf(s.charAt(i)).toLowerCase();
        return answer;
    }
}