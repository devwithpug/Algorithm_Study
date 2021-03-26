// 프로그래머스 DFS/BFS 03 단어 변환
// 문제 설명
// 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
// 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
// 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
// 2. words에 있는 단어로만 변환할 수 있습니다.
// 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 
// "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
// 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 
// begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.
// 제한사항
//     각 단어는 알파벳 소문자로만 이루어져 있습니다.
//     각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
//     words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
//     begin과 target은 같지 않습니다.
//     변환할 수 없는 경우에는 0를 return 합니다.
// 입출력 예
// begin 	target 	words 	return
// "hit" 	"cog" 	["hot", "dot", "dog", "lot", "log", "cog"] 	4
// "hit" 	"cog" 	["hot", "dot", "dog", "lot", "log"] 	0
package io.github.devwithpug;

import java.util.Arrays;

class DFS_BFS_03_Solution {
    private static boolean findDiffer(String word, String target) {
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == target.charAt(i))
                count++;
        }
        if (count == word.length() - 1)
            return true;
        else
            return false;
    }

    private static int find(int answer, boolean[] chk, String begin, String target, String[] words) {
        if (!Arrays.stream(words).anyMatch(target::equals))
            return 0;
        if (findDiffer(begin, target))
            return answer + 1;
        for (int i = 0; i < words.length; i++) {
            if (findDiffer(begin, words[i]) && !chk[i]) {
                chk[i] = true;
                return find(answer + 1, chk, words[i], target, words);
            }
        }
        return 0;
    }

    public int solution(String begin, String target, String[] words) {
        boolean[] chk = new boolean[words.length];
        return find(0, chk, begin, target, words);
    }
}

public class Prog_DFS_BFS_03 {
    public static void main(String[] args) {
        DFS_BFS_03_Solution s = new DFS_BFS_03_Solution();
        String begin = "hit";
        String target = "cog";
        String[] words = { "hot", "dot", "dog", "lot", "log", "cog" };
        System.out.println(s.solution(begin, target, words));
    }
}
