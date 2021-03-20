// 프로그래머스 완전탐색 01 모의고사
// 문제 설명
// 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
// 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
// 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
// 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
// 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
// 제한 조건
// 시험은 최대 10,000 문제로 구성되어있습니다.
// 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
// 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
// 입출력 예
// answers	return
// [1,2,3,4,5]	[1]
// [1,3,2,4,2]	[1,2,3]
// 입출력 예 설명
// 입출력 예 #1
// 수포자 1은 모든 문제를 맞혔습니다.
// 수포자 2는 모든 문제를 틀렸습니다.
// 수포자 3은 모든 문제를 틀렸습니다.
// 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.
// 입출력 예 #2
// 모든 사람이 2문제씩을 맞췄습니다.

package io.github.devwithpug;

import java.util.ArrayList;
import java.util.Arrays;

class Student {
    private int id;
    private int score;
    private int answer;
    private int prev_answer;

    public Student(int id, int s, int a, int p) {
        this.id = id;
        this.score = s;
        this.answer = a;
        this.prev_answer = p;
    }

    public int g_i() {
        return this.id;
    }

    public int g_s() {
        return this.score;
    }

    public int g_a() {
        return this.answer;
    }

    public int g_p() {
        return this.prev_answer;
    }

    public void add_s() {
        this.score++;
    }

    public void s_a(int a) {
        this.prev_answer = this.answer;
        this.answer = a;
    }
}

class ExhaustiveSearch_01_Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        Student s1 = new Student(1, 0, 1, 0);
        Student s2 = new Student(2, 0, 2, 5);
        Student s3 = new Student(3, 0, 3, 3);
        int idx = 1;
        for (int item : answers) {
            if (item == s1.g_a()) {
                s1.add_s();
            }
            if (item == s2.g_a()) {
                s2.add_s();
            }
            if (item == s3.g_a()) {
                s3.add_s();
            }
            s1.s_a((s1.g_a() == 5) ? 1 : s1.g_a() + 1);

            s2.s_a((idx % 2 == 0) ? 2 : (s2.g_p() == 1) ? 3 : (s2.g_p() == 3) ? 4 : (s2.g_p() == 4) ? 5 : 1);
            s3.s_a((idx % 2 == 0)
                    ? (s3.g_p() == 3) ? 1 : (s3.g_p() == 1) ? 2 : (s3.g_p() == 2) ? 4 : (s3.g_p() == 4) ? 5 : 3
                    : s3.g_a());
            idx++;
        }

        Student max = Arrays.stream(new Student[] { s1, s2, s3 }).max((o1, o2) -> o1.g_s() - o2.g_s()).get();
        answer.add(max.g_i());
        for (Student s : new Student[] { s1, s2, s3 }) {
            if (max.g_i() == s.g_i()) {
                continue;
            }
            if (max.g_s() == s.g_s()) {
                answer.add(s.g_i());
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}

public class Prog_ExhaustiveSearch_01 {
    public static void main(String[] args) {
        ExhaustiveSearch_01_Solution s = new ExhaustiveSearch_01_Solution();
        int[] answers = { 1, 3, 2, 4, 2 };
        System.out.println(Arrays.toString(s.solution(answers)));
    }
}
