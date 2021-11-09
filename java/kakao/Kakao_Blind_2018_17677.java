// 2018 KAKAO BLIND RECRUITMENT 1차 다트 게임
// https://programmers.co.kr/learn/courses/30/lessons/17677

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int solution(String str1, String str2) {
        Map<String, Integer> map1 = extract(str1);
        Map<String, Integer> map2 = extract(str2);

        Set<String> keys = new HashSet<>(map1.keySet());
        keys.addAll(map2.keySet());

        double resultMin = 0;
        double resultMax = 0;

        for (String key : keys) {
            resultMin += Math.min(map1.getOrDefault(key, 0), map2.getOrDefault(key, 0));
            resultMax += Math.max(map1.getOrDefault(key, 0), map2.getOrDefault(key, 0));
        }
        return (keys.size() == 0) ? 65536 : (int) (resultMin / resultMax * 65536);
    }

    private Map<String, Integer> extract(String s) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length() - 1; i++) {
            String sub = (Character.isLetter(s.charAt(i)) && Character.isLetter(s.charAt(i+1))) ? s.substring(i, i + 2).toUpperCase() : null;

            if (sub != null) {
                if (map.containsKey(sub)) {
                    map.put(sub, map.get(sub) + 1);
                } else {
                    map.put(sub, 1);
                }
            }
        }
        return map;
    }
}