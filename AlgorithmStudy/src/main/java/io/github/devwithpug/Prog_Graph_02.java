// 프로그래머스 그래프 02 순위
// 문제 설명
// n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 
// 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 
// 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
// 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 
// 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.
// 제한사항
//     선수의 수는 1명 이상 100명 이하입니다.
//     경기 결과는 1개 이상 4,500개 이하입니다.
//     results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
//     모든 경기 결과에는 모순이 없습니다.
// 입출력 예
// n 	results 	return
// 5 	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]] 	2
package io.github.devwithpug;

class Graph_02_Solution {
    static int findParents(int n, int[][] results, boolean[] visited, int num) {
        if (visited[n])
            return 0;
        visited[n] = true;
        for (int[] path : results) {
            if (path[1] - 1 == n && !visited[path[0] - 1]) {
                num = 1 + findParents(path[0] - 1, results, visited, num);
            }
        }
        return num;
    }

    static int findChilds(int n, int[][] results, boolean[] visited, int num) {
        if (visited[n])
            return 0;
        visited[n] = true;
        for (int[] path : results) {
            if (path[0] - 1 == n && !visited[path[1] - 1]) {
                num = 1 + findChilds(path[1] - 1, results, visited, num);
            }
        }
        return num;
    }

    public int solution(int n, int[][] results) {
        int answer = 0;
        int[] parents = new int[n];
        int[] childs = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = findParents(i, results, new boolean[n], 0);
            childs[i] = findChilds(i, results, new boolean[n], 0);
        }
        for (int i = 0; i < n; i++) {
            if (parents[i] + childs[i] == n - 1)
                answer++;
        }
        return answer;
    }
}

public class Prog_Graph_02 {
    public static void main(String[] args) {
        int n = 5;
        int[][] results = { { 4, 3 }, { 4, 2 }, { 3, 2 }, { 1, 2 }, { 2, 5 } };
        Graph_02_Solution s = new Graph_02_Solution();
        System.out.println(s.solution(n, results));
    }
}
