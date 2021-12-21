/**
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are required to print the elements of array from end to beginning each in a separate line.
4. For the above purpose complete the body of displayArrReverse function. Don't change the signature.*/

 /**
 * ANSWER
 */

import java.io.*;
import java.util.*;

public class Display_Array_In_Reverse {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];

    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }

    displayArrReverse(arr, 0);
  }

  public static void displayArrReverse(int[] arr, int idx) {
    if (idx == arr.length) {
      return;
    }

    displayArrReverse(arr, idx + 1);
    System.out.println(arr[idx]);
  }

}

 /**
 * SOURCE-PEPCODING
 */