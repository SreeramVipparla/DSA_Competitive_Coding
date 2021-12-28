/**
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

 

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true
 

Constraints:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
 /**
 * ANSWER
 */

import java.io.*;
import java.util.*;

public class Can_I_Win {

  public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
    if((1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal)    return false;
    return canWin(0, desiredTotal, maxChoosableInteger,  new HashMap<Integer, Boolean>());
}

private boolean canWin(int state, int total, int max,  Map<Integer, Boolean> dp){
    if(dp.containsKey(state))   return dp.get(state);
    
    for(int i=max;i>=1;i--){
        if( (state&(1<<i))==0 && (total-i<=0 || !canWin(state|(1<<i), total-i, max,  dp))){
            return dp.computeIfAbsent(state, k->true);
        }
    }
    return dp.computeIfAbsent(state, k->false);
}

}

 /**
 * SOURCE-PEPCODING
 */