"""
QUESTION-
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.
"""
"""
ANSWER-
"""
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        mp = {}
        for c in s:
           mp.setdefault(c, 0)
           mp[c] += 1
           
        ans = [0] * 10
        self.dfs(mp, ans)
        return "".join([str(num) * ans[num] for num, count in enumerate(ans)])
        
    def dfs(self, mp, ans):
        str_to_digit = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
        while mp != {}:
            if 'z' in mp:
                t = 0
            elif 'w' in mp:
                t = 2
            elif 'u' in mp:
                t = 4
            elif 'f' in mp:
                t = 5
            elif 'x' in mp:
                t = 6
            elif 'g' in mp:
                t = 8
            elif 'v' in mp:
                t = 7
            elif 'o' in mp:
                t = 1
            elif 't' in mp:
                t = 3
            else:
                t = 9
            for c in str_to_digit[t]:
                mp[c] -= 1
                if mp[c] == 0:
                    del mp[c]
            ans[t] += 1
        return ans
"""
SOURCE-LEETCODE
"""