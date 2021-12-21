/**
 * QUESTION

1. You are given a number n.
2. You've to write code to print the pattern given in output format below.
     1
  2  3  2
3 4  5  4  3
  2  3  2
     1


 */


 /**
 * ANSWER
 */
 import java.util.*;

public class pattern15{

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        int n = scn.nextInt();
        int stars = 1;
        int spaces = n / 2;
        int oval = 1;
        for(int i = 1; i <= n; i++){
            int val = oval;
            for(int j = 1;  j <= spaces; j++){
                System.out.print("\t");
            }
            for(int j = 1;  j <= stars; j++){
                System.out.print(val + "\t");
                if(j <= stars / 2){
                    val++;
                }else{
                    val--;
                }
            }
            System.out.println();
            if(i <= n / 2){
                oval++;
                stars += 2;
                spaces--;
            }else{
                oval--;
                stars -= 2;
                spaces++;
            }
        }
    }
}
 /**
 * SOURCE-PEPCODING
 */