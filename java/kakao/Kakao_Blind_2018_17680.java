// 2018 KAKAO BLIND RECRUITMENT 1차 캐시
// https://programmers.co.kr/learn/courses/30/lessons/17680

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Map<String, Integer> cache = new HashMap<>();

        for (String city : cities) {
                city = city.toLowerCase();

            if (cache.containsKey(city)) {
                answer += 1;
            } else if (cache.size() >= cacheSize) {
                cache.remove(
                        cache.keySet().stream()
                                .reduce((r, n) -> (cache.get(r) > cache.get(n)) ? r : n)
                                .orElse("")
                );
                answer += 5;
            } else {
                answer += 5;
            }
            if (cacheSize != 0) {
                cache.put(city, 0);
            }
            cache.keySet().forEach(k -> cache.put(k, cache.get(k)+1));
        }
        return answer;
    }
}