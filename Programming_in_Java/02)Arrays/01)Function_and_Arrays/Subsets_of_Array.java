/**
 * QUESTION
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are required to print all subsets of arr. Each subset should be
on separate line. For more clarity check out sample input and output. */


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];
    for(int i = 0; i < n; i++){
       arr[i] = Integer.parseInt(br.readLine());
    }

    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < (1 << arr.length); i++){
       int dec = i;
       String str = "";

       for(int j = 0; j < arr.length; j++){
          int r = dec % 2;
          dec = dec / 2;

          if(r == 0){
            str = "-\t" + str;
          } else {
            str = arr[arr.length - 1 - j] + "\t" + str;
          }
       }

       sb.append(str + "\n");
    }

    System.out.println(sb);
 }

}
 /**
 * SOURCE-PEPCODING
 */