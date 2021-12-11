/**
 * QUESTION
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are required to print an inverted bar chart representing value of arr a.
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

    int max = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(br.readLine());
      max = Math.max(max, arr[i]);
    }

    for (int i = 0; i < max; i++) {
      for (int val : arr) {
        if (i < val) {
          System.out.print("*\t");
        } else {
          System.out.print("\t");
        }
      }

      System.out.println();
    }
  }

}

 /**
 * SOURCE-PEPCODING
 */