"""
QUESTION-

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

"""
"""
ANSWER-
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
            dictionary = dict(Counter(s))
            print(dictionary)
            largest_palindrome = 0
            count_odd_once = False
            for i in dictionary:
                if dictionary[i] % 2 == 0:
                    largest_palindrome += dictionary[i]
                else:
                    if count_odd_once is False:
                        count_odd_once = True
                        largest_palindrome += dictionary[i]
                    else:
                        largest_palindrome += dictionary[i] - 1
            return largest_palindrome
"""            
SOURCE-LEETCODE
"""