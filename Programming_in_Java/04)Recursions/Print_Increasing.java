/**
1. You are given a positive number n. 
2. You are required to print the counting from 1 to n.
3. You are required to not use any loops. Complete the body of print Increasing function to achieve it. Don't change the signature of the function.*/

 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Print_Increasing{

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    printIncreasing(n);
  }

  public static void printIncreasing(int n) {
    if(n == 0){
      return;
    }
    
    printIncreasing(n - 1);
    System.out.println(n);
  }

}

 /**
 * SOURCE-PEPCODING
 */