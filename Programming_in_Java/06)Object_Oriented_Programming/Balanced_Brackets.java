
/**
1. You are given a string exp representing an expression.
2. You are required to check if the expression is balanced i.e. closing brackets and opening brackets match up well.

e.g.
[(a + b) + {(c + d) * (e / f)}] -> true
[(a + b) + {(c + d) * (e / f)]} -> false
[(a + b) + {(c + d) * (e / f)} -> false
([(a + b) + {(c + d) * (e / f)}] -> false
 /**
 * ANSWER
 */

import java.io.*;
import java.util.*;
public class Balanced_Brackets {
  

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();

    Stack<Character> st = new Stack<>();
    for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);
        if (ch == '(' || ch == '{' || ch == '[') {
            st.push(ch);
        } else if (ch == ')') {
            if (st.size() == 0 || st.peek() != '(') {
                System.out.println(false);
                return;
            } else {
                st.pop();
            }
        } else if (ch == '}') {
            if (st.size() == 0 || st.peek() != '{') {
                System.out.println(false);
                return;
            } else {
                st.pop();
            }
        } else if (ch == ']') {
            if (st.size() == 0 || st.peek() != '[') {
                System.out.println(false);
                return;
            } else {
                st.pop();
            }
        } else {
            // nothing
        }
    }

    if (st.size() == 0) {
        System.out.println(true);
    } else {
        System.out.println(false);
    }
}
}

 /**
 * SOURCE-PEPCODING
 */