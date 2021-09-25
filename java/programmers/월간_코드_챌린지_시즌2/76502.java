// 월간 코드 챌린지 시즌2 괄호 회전하기 https://programmers.co.kr/learn/courses/30/lessons/76502

import java.util.Stack;

class Solution {
    private boolean isValid(String[] split) {
        Stack<String> stack = new Stack<>();

        for (String s : split) {
            if (s.equals("(") || s.equals("{") || s.equals("[")) {
                stack.push(s);
            } else {
                if (stack.empty()) return false;
                if (s.equals(")") && !stack.pop().equals("(")) return false;
                if (s.equals("}") && !stack.pop().equals("{")) return false;
                if (s.equals("]") && !stack.pop().equals("[")) return false;
            }
        }
        return stack.empty();
    }

    public int solution(String s) {
        int answer = 0;

        String[] split = s.split("");
        for (int i = 0; i < split.length; i++) {
            String tmp = split[0];
            for (int j = 0; j < split.length-1; j++) {
                split[j] = split[j + 1];
            }
            split[split.length - 1] = tmp;

            if (isValid(split)) answer++;
        }
        return answer;
    }
}
