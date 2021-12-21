/**
1. You are given a string str.
2. Complete the body of printPermutations function - without changing signature - to calculate and print all permutations of str.
Use sample input and output to take idea about permutations.

 /**
 * ANSWER
 */

import java.io.*;
import java.util.*;

public class Print_Permutations {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    printPermutations(str, "");
}

public static void printPermutations(String ques, String ans){
    if(ques.length() == 0){
        System.out.println(ans);
        return;
    }

    for(int i = 0; i < ques.length(); i++){
        char ch = ques.charAt(i);
        String roq = ques.substring(0, i) + ques.substring(i + 1);
        printPermutations(roq, ans + ch);
    }
}
}
 /**
 * SOURCE-PEPCODING
 */