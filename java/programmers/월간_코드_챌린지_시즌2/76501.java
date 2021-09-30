// 월간 코드 챌린지 시즌2 음양더하기 https://programmers.co.kr/learn/courses/30/lessons/76501

class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        for (int i = 0; i < signs.length; i++) answer += (signs[i]) ? absolutes[i] : -absolutes[i];
        return answer;
    }
}