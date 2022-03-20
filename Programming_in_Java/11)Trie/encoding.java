/**
1. You are given a string str of digits. (will never start with a 0)
2. You are required to encode the str as per following rules
    1 -> a
    2 -> b
    3 -> c
    ..
    25 -> y
    26 -> z
3. Complete the body of printEncodings function - without changing signature - to calculate and print all encodings of str.
Use the input-output below to get more understanding on what is required
123 -> abc, aw, lc
993 -> iic
013 -> Invalid input. A string starting with 0 will not be passed.
103 -> jc
303 -> No output possible. But such a string maybe passed. In this case print nothing.

 /**
 * ANSWER
 */

import java.io.*;
import java.util.*;


public class Print_Encodings {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    printEncodings(str, "");
}

public static void printEncodings(String ques, String ans) {
    if (ques.length() == 0) {
        System.out.println(ans);
        return;
    } else if (ques.length() == 1) {
        if (ques.charAt(0) == '0') {
            return;
        } else {
            String ch0 = ques.substring(0, 1);
            String roq0 = ques.substring(1);
            String code0 = (char)('a' + (Integer.parseInt(ch0) - 1)) + "";
            printEncodings(roq0, ans + code0);
        }
    } else {
        if (ques.charAt(0) == '0') {
            return;
        } else {
            String ch0 = ques.substring(0, 1);
            String roq0 = ques.substring(1);
            String code0 = (char)('a' + (Integer.parseInt(ch0) - 1)) + "";
            printEncodings(roq0, ans + code0);

            String ch01 = ques.substring(0, 2);
            String roq01 = ques.substring(2);
            String code01 = (char)('a' + (Integer.parseInt(ch01) - 1)) + "";

            if (Integer.parseInt(ch01) <= 26) {
                printEncodings(roq01, ans + code01);
            }
        }
    }
}
}

 /**
 * SOURCE-PEPCODING
 */
