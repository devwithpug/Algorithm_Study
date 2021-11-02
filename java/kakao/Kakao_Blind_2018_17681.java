// 2018 KAKAO BLIND RECRUITMENT 1차 비밀 지도
// https://programmers.co.kr/learn/courses/30/lessons/17681

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];

        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder(Integer.toBinaryString(arr1[i] | arr2[i]));

            while (sb.length() < n) {
                sb.insert(0, "0");
            }
            
            StringBuilder decoded = new StringBuilder();
            for (int j = 0; j < n; j++) {
                decoded.append((sb.charAt(j) == '1') ? "#" : " ");
            }
            answer[i] = decoded.toString();
        }

        return answer;
    }
}
