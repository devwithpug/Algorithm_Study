package io.github.devwithpug;

// 프로그래머스 코딩테스트 해시 01 완주하지 못한 선수
// 문제 설명
// 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
// 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
// 제한사항
// 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
// completion의 길이는 participant의 길이보다 1 작습니다.
// 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
// 참가자 중에는 동명이인이 있을 수 있습니다.
// 입출력 예
// participant	completion	return
// ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
// ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
// ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map.Entry;

class SolutionClass {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);

        for (int i = 0; i < participant.length - 1; i++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            }
        }
        return participant[participant.length - 1];
    }
}

class SolutionHashMap {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        for (String player : participant)
            hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion)
            hm.put(player, hm.get(player) - 1);

        for (Entry<String, Integer> entry : hm.entrySet()) {
            if (entry.getValue() != 0)
                answer = entry.getKey();
        }
        return answer;
    }
}

public class Prog_Hash_01 {
    public static void main(String[] args) {
        String[] participant = { "marina", "josipa", "nikola", "vinko", "filipa" };
        String[] completion = { "josipa", "filipa", "marina", "nikola" };
        // Using String Sort
        SolutionClass s1 = new SolutionClass();
        long s_t = System.nanoTime();
        System.out.println("answer: " + s1.solution(participant, completion));
        long t_t = System.nanoTime();
        System.out.println(t_t - s_t + " ns");
        // Using HashMap
        SolutionHashMap s2 = new SolutionHashMap();
        s_t = System.nanoTime();
        System.out.println("answer: " + s2.solution(participant, completion));
        t_t = System.nanoTime();
        System.out.println(t_t - s_t + " ns");
    }
}
