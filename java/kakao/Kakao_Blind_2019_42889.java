// 2019 KAKAO BLIND RECRUITMENT 실패율 https://programmers.co.kr/learn/courses/30/lessons/42889

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int N, int[] stages) {
        Map<Integer, Double> result = new HashMap<>();
        int[][] status = new int[N][2];

        for (int stage : stages) {
            if (stage > N) {
                for (int i = 0; i < N; i++) {
                    status[i][1]++;
                }
            } else {
                for (int i = 0; i < stage; i++) {
                    status[i][1]++;
                }
                status[stage-1][0]++;
            }
        }

        for (int i = 0; i < status.length; i++) {
            result.put(i+1, (status[i][1] == 0) ? 0.0 : (double)status[i][0] / (double)status[i][1]);
        }

        List<Integer> collect = result.entrySet().stream()
                .sorted((r1, r2) -> r2.getValue().compareTo(r1.getValue()))
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());

        return collect.stream().mapToInt(i -> i).toArray();
    }
}