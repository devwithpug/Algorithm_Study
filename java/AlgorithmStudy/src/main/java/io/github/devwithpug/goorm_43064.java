// goorm Binary Search
// https://level.goorm.io/exam/43064/binary-search/quiz/1
package io.github.devwithpug;

import java.io.*;

public class goorm_43064 {

    private static void binary_search(int k, String[] arr, int a, int b) {
        if (a > b) {
            System.out.println("X");
            return;
        }

        int mid = (a + b) / 2;

        if (k < Integer.parseInt(arr[mid]))
            binary_search(k, arr, a, mid - 1);
        else if (k > Integer.parseInt(arr[mid]))
            binary_search(k, arr, mid + 1, b);
        else if (k == Integer.parseInt(arr[mid]))
            System.out.println(mid + 1);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");
        int k = Integer.parseInt(br.readLine());

        binary_search(k, arr, 0, n - 1);
    }
}
