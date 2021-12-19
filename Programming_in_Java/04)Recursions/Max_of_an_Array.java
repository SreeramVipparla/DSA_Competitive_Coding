/**
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are required to find the maximum of input. 
4. For the purpose complete the body of maxOfArray function. Don't change the signature.
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

      int max = maxOfArray(arr, 0);
      System.out.println(max);
   }

   public static int maxOfArray(int[] arr, int idx) {
      if(idx == arr.length - 1){
         return arr[idx];
      }
      
      int misa = maxOfArray(arr, idx + 1);
      if(misa > arr[idx]){
         return misa;
      } else {
         return arr[idx];
      }
   }

}
 /**
 * SOURCE-PEPCODING
 */