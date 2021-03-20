// 프로그래머스 완전탐색 02 소수 찾기
// 문제 설명
// 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
// 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
// 제한사항
// numbers는 길이 1 이상 7 이하인 문자열입니다.
// numbers는 0~9까지 숫자만으로 이루어져 있습니다.
// "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
// 입출력 예
// numbers	return
// "17"	3
// "011"	2
// 입출력 예 설명
// 예제 #1
// [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
// 예제 #2
// [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
// 11과 011은 같은 숫자로 취급합니다.

package io.github.devwithpug;

import java.util.ArrayList;
import java.util.Arrays;

class ExhaustiveSearch_02_Solution {
    static ArrayList<Integer> answer = new ArrayList<Integer>();

    public int solution(String numbers) {
        String[] number_arr = numbers.split("");
        Arrays.stream(number_arr).map(i -> Integer.parseInt(i));
        ArrayList<String> list = new ArrayList<String>(Arrays.asList(number_arr));
        ArrayList<String> result = new ArrayList<String>();

        for (int i = 0; i < numbers.length(); i++) {
            search(list, result, numbers.length(), i + 1);
        }
        return answer.size();
    }

    private void search(ArrayList<String> list, ArrayList<String> result, int n, int r) {
        if (r == 0) {
            String out = "";
            for (String c : result) {
                out += c;
            }
            int num = Integer.parseInt(out);
            if (!answer.contains(num)) {
                if (prime(num)) {
                    answer.add(num);
                }
            }

        } else {
            for (int i = 0; i < n; i++) {
                result.add(list.remove(i));
                System.out.println(n + "P" + r);
                System.out.println(result.toString());
                search(list, result, n - 1, r - 1);
                list.add(i, result.remove(result.size() - 1));
            }
        }
    }

    private boolean prime(int num) {
        if (num > 1) {
            for (int i = 2; i * i <= num; i++) {
                if (num % i == 0) {
                    return false;
                }
            }
        } else {
            return false;
        }
        return true;
    }
}

public class Prog_ExhaustiveSearch_02 {
    public static void main(String[] args) {
        ExhaustiveSearch_02_Solution s = new ExhaustiveSearch_02_Solution();
        System.out.println(s.solution("17"));
    }
}
