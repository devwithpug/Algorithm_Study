// 모음 사전 https://programmers.co.kr/learn/courses/30/lessons/84512
// 문제 설명
// 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
// 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.
// 제한사항
// word의 길이는 1 이상 5 이하입니다.
// word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
// 입출력 예
// word	result
// "AAAAE"	6
// "AAAE"	10
// "I"	1563
// "EIO"	1189

class Solution {

    private final String[] ALPHA = {"A", "E", "I", "O", "U"};

    public int solution(String word) {
        int answer = 0;
        String[] tmp = {"", "", "", "", ""};

        for (int a = 0; a < 5; a++) {
            makeEmptyFrom(tmp, 0);
            tmp[0] = ALPHA[a];
            answer++;
            if (String.join("", tmp).equals(word)) return answer;
            
            for (int b = 0; b < 5; b++) {
                makeEmptyFrom(tmp, 1);
                tmp[1] = ALPHA[b];
                answer++;
                if (String.join("", tmp).equals(word)) return answer;

                for (int c = 0; c < 5; c++) {
                    makeEmptyFrom(tmp, 2);
                    tmp[2] = ALPHA[c];
                    answer++;
                    if (String.join("", tmp).equals(word)) return answer;

                    for (int d = 0; d < 5; d++) {
                        makeEmptyFrom(tmp, 3);
                        tmp[3] = ALPHA[d];
                        answer++;
                        if (String.join("", tmp).equals(word)) return answer;

                        for (int e = 0; e < 5; e++) {
                            makeEmptyFrom(tmp, 4);
                            tmp[4] = ALPHA[e];
                            answer++;
                            if (String.join("", tmp).equals(word)) return answer;
                        }
                    }
                }
            }
        }
        return answer;
    }

    private void makeEmptyFrom(String[] arr, int from) {
        for (int i = from; i <= 4; i++) {
            arr[i] = "";
        }
    }
}