/**
 * QUESTION

1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are required to print the elements of array from beginning to end each in a separate line.
4. For the above purpose complete the body of displayArr function. Don't change the signature.
 */


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];

    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }

    displayArr(arr, 0);
  }

  public static void displayArr(int[] arr, int idx) {
    if (idx == arr.length) {
      return;
    }

    System.out.println(arr[idx]);
    displayArr(arr, idx + 1);
  }

}
 /**
 * HINTS-use bufferrader anfd use conditionals to solve the problem
 */

 /**
 * SOURCE-PEPCODING
 */