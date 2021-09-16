// 2019 KAKAO WINTER INTERNSHIP 튜플 https://programmers.co.kr/learn/courses/30/lessons/64065

import java.util.*;

class Solution {
    public int[] solution(String s) {

        Map<Integer, Integer> map = new HashMap<>();

        String[] split = s.split("");
        String tmp = "";
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                tmp += split[i];
            } else if (!tmp.equals("")){
                map.put(Integer.parseInt(tmp), map.getOrDefault(Integer.parseInt(tmp), 0) + 1);
                tmp = "";
            }
        }

        return map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .mapToInt(Map.Entry::getKey)
                .toArray();
    }
}