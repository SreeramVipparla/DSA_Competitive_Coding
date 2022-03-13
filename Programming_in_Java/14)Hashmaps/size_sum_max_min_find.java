/**
 * QUESTION

1. You are given a string that contains only lowercase and uppercase alphabets. 
2. You have to toggle the case of every character of the given string.*/


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Main {

	public static String toggleCase(String str){
		StringBuilder ans = new StringBuilder();
		for(int i = 0 ; i < str.length(); i++){
			char ch = str.charAt(i);
			if(ch >= 'a' && ch <= 'z'){
				ans.append((char)(ch - 'a' + 'A') + "");
			}else{
				ans.append((char)(ch - 'A' +'a') + "");
			}
		}
		return ans.toString();
	}
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		String str = scn.next();
		System.out.println(toggleCase(str));
	}

}

 /**
 * SOURCE-PEPCODING
 */