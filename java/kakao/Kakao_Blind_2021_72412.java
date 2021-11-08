// 2021 KAKAO BLIND RECRUITMENT 순위 검색
// https://programmers.co.kr/learn/courses/30/lessons/72412

import java.util.*;

class Solution {

    private void comb(String s, int d, String[] info, Map<String, List<Integer>> map) {
        if (d == 4) {
            int score = Integer.parseInt(info[4]);
            if (!map.containsKey(s)) {
                map.put(s, new ArrayList<>());
            }
            map.get(s).add(score);
        } else {
            comb(s + "-", d+1, info, map);
            comb(s + info[d], d+1, info, map);
        }
    }

    private int search(String q, int score, Map<String, List<Integer>> map) {
        if (!map.containsKey(q)) {
            return 0;
        }
        List<Integer> scores = map.get(q);

        int start = 0;
        int end = scores.size() - 1;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (scores.get(mid) < score) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return scores.size() - start;
    }

    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        Map<String, List<Integer>> map = new HashMap<>();

        Arrays.stream(info).forEach(i -> comb("", 0, i.split(" "), map));

        map.keySet().forEach(k -> Collections.sort(map.get(k)));

        for (int i = 0; i < query.length; i++) {
            String tmp = query[i].replace(" and ", "");
            String[] q = tmp.split(" ");
            answer[i] = search(q[0], Integer.parseInt(q[1]), map);
        }
        return answer;
    }
}