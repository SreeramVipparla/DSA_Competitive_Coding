

/**
QUESTION
1. You are given a number n, representing the number of friends.
2. Each friend can stay single or pair up with any of it's friends.
3. You are required to print the number of ways in which these friends can stay single or pair up.
E.g.
1 person can stay single or pair up in 1 way.
2 people can stay singles or pair up in 2 ways. 12 => 1-2, 12.
3 people (123) can stay singles or pair up in 4 ways. 123 => 1-2-3, 12-3, 13-2, 23-1.
 /**
 * ANSWER
 */
import java.io.*;


public class Friends_Pairing {
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    if (n <= 2) {
       System.out.println(n);
       return;
    }

    long[] arr = new long[n + 1];
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 2;

    for (int i = 3; i <= n; i++) {
       arr[i] = arr[i - 1] + (i - 1) * arr[i - 2];
    }

    System.out.println(arr[n]);
 }
}

 /**
 * SOURCE-PEPCODING
 */