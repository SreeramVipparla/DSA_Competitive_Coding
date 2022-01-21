"""
QUESTION-
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
"""
ANSWER-
"""
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount, sCount = {},{}
        
        result = []
        

        pCount = collections.Counter(p)
        sCount = collections.Counter(s[:len(p)])
        i = 0
        j = len(p)
        while j <= len(s):
            
            if pCount == sCount:
                result.append(i)
            sCount[s[i]] -= 1
            if sCount[s[i]] <= 0:
                sCount.pop(s[i])
            if j < len(s):
                sCount[s[j]] = 1 + sCount.get(s[j], 0)
                
            i += 1
            j += 1
            
        return result
"""
SOURCE-LEETCODE
"""