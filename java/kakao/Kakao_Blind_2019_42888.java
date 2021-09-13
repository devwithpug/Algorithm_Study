// 2019 KAKAO BLIND RECRUITMENT 오픈채팅방
// https://programmers.co.kr/learn/courses/30/lessons/42888

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String[] solution(String[] record) {
        Map<String, String> map = new HashMap<>();

        Arrays.stream(record)
                .forEach(re -> {
                    String[] split = re.split(" ");
                    if (split[0].equals("Enter") || split[0].equals("Change")) {
                        map.put(split[1], split[2]);
                    }
                });

        return Arrays.stream(record)
                .filter(re -> !re.split(" ")[0].equals("Change"))
                .map(re -> {
                    String[] split = re.split(" ");
                    if (split[0].equals("Enter")) return map.get(split[1]) + "님이 들어왔습니다.";
                    else return map.get(split[1]) + "님이 나갔습니다.";
                }).toArray(String[]::new);
    }
}