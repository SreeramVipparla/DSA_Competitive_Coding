/**
1. You are given a string str.
2. Complete the body of getSS function - without changing signature - to calculate all subsequences of str.
Use sample input and output to take idea about subsequences.
/**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Get_Subsequence{

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        ArrayList<String> ss = gss(str);
        System.out.println(ss);
    }

    public static ArrayList<String> gss(String str) {
        if(str.length() == 0){
            ArrayList<String> bres = new ArrayList<>();
            bres.add("");
            return bres;
        }

        char ch = str.charAt(0);
        String ros = str.substring(1);

        ArrayList<String> rres = gss(ros);
        ArrayList<String> mres = new ArrayList<>();

        for(String rstr: rres){
            mres.add(rstr);
        }

        for(String rstr: rres){
            mres.add(ch + rstr);
        }
        return mres;
    }
}


 /**
 * SOURCE-PEPCODING
 */