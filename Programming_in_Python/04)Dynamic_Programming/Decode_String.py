"""
QUESTION-
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 


"""
"""
ANSWER-
"""
class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        for i in s:

            if i==']':
                pos = len(ans)-1
                temp = ""
                while ans[pos]!='[':
                    temp = ans[pos] +temp
                    pos-=1
                num = 0
                pos-=1
                c = 1
                while pos>=0 and ans[pos] in "0123456789":
                    num+= c*(ord(ans[pos])-ord("0"))
                    pos-=1
                    c*=10

                ans = ans[:pos+1]+temp*num
            else:
                ans+=i
        return ans
"""
SOURCE-LEETCODE
"""