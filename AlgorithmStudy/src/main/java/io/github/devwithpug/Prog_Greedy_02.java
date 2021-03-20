// 프로그래머스 그리디 02 조이스틱
// 문제 설명
// 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
// ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
// 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
// ▲ - 다음 알파벳
// ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
// ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
// ▶ - 커서를 오른쪽으로 이동
// 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
// - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
// - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
// - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
// 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
// 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
// 제한 사항
// name은 알파벳 대문자로만 이루어져 있습니다.
// name의 길이는 1 이상 20 이하입니다.
// 입출력 예
// name	return
// "JEROEN"	56
// "JAN"	23
package io.github.devwithpug;

import java.util.ArrayList;

class Greedy_02_Solution {
    public int solution(String name) {
        int answer = 0;
        char[] arr = name.toCharArray();
        ArrayList<Integer> idx_list = new ArrayList<Integer>();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 'A') {
                idx_list.add(i);
            }
        }
        int idx = 0;
        while (!idx_list.isEmpty() && idx >= 0) {
            if (arr[idx] != 'A') {
                answer += (arr[idx] - 'A' < 'Z' - arr[idx] + 1) ? arr[idx] - 'A' : 'Z' - arr[idx] + 1;
                idx_list.remove(idx_list.indexOf(idx));
            }
            if (idx_list.isEmpty()) {
                break;
            }
            int left_diff = (idx_list.get(idx_list.size() - 1) < idx) ? idx - idx_list.get(idx_list.size() - 1)
                    : arr.length - idx_list.get(idx_list.size() - 1) + idx;
            int right_diff = (idx_list.get(0) > idx) ? idx_list.get(0) - idx : arr.length - idx + idx_list.get(0);
            if (left_diff < right_diff) {
                idx = idx_list.get(idx_list.size() - 1);
                answer += left_diff;
            } else {
                idx = idx_list.get(0);
                answer += right_diff;
            }
        }
        return answer;
    }
}

public class Prog_Greedy_02 {
    public static void main(String[] args) {
        Greedy_02_Solution s = new Greedy_02_Solution();
        System.out.println(s.solution("BABAAAAB"));
    }
}
