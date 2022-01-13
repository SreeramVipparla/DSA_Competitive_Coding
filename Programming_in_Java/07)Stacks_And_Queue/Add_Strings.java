"""
QUESTION-
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""
"""
ANSWER-
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1)-1, len(num2)-1
        ret = []
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry:
            d1 = int(num1[p1]) if p1 >= 0 else 0
            d2 = int(num2[p2]) if p2 >= 0 else 0
            sum = d1+d2+carry
            carry, digit = sum//10, sum%10
            ret.append(str(digit))
            p1 -= 1
            p2 -= 1
            
        return "".join(ret[::-1])
"""
SOURCE-LEETCODE
"""