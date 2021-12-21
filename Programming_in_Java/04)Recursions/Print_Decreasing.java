/**
1. You are given a positive number n. 
2. You are required to print the counting from n to 1.
3. You are required to not use any loops. Complete the body of print Decreasing function to achieve it.
*/

 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Print_Decreasing{

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    printDecreasing(n);
  }

  public static void printDecreasing(int n) {
    if(n == 0){
      return;
    }
    
    System.out.println(n);
    printDecreasing(n - 1);
  }

}

 /**
 * SOURCE-PEPCODING
 */