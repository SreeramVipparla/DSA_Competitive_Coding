/**
1. You are given a positive number n. 
2. You are required to print the counting from n to 1 and back to n again.
3. You are required to not use any loops. Complete the body of pdi function to achieve it. Don't change the signature of the function.
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
    pdi(n);
  }

  public static void pdi(int n) {
    if(n == 0){
      return;
    }
    
    System.out.println(n);
    pdi(n - 1);
    System.out.println(n);
  }

}
 /**
 * SOURCE-PEPCODING
 */