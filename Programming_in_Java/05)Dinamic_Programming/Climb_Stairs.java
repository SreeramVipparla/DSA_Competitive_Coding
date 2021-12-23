


/**
QUESTION
1. You are given a number n, representing the number of stairs in a staircase.
2. You are on the 0th step and are required to climb to the top.
3. In one move, you are allowed to climb 1, 2 or 3 stairs.
4. You are required to print the number of different paths via which you can climb to the top.
 /**
 * ANSWER
 */
import java.io.*;


public class Climb_Stairs {

   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int n = Integer.parseInt(br.readLine());
      long[] arr = new long[n + 1];
      arr[0] = 1;

      for (int i = 1; i <= n; i++) {
         if(i >= 1){
            arr[i] += arr[i - 1];
         }

         if(i >= 2){
            arr[i] += arr[i - 2];
         }

         if(i >= 3){
            arr[i] += arr[i - 3];
         }
      }

      System.out.println(arr[n]);
   }

}

 /**
 * SOURCE-PEPCODING
 */