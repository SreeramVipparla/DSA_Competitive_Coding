"""
QUESTION-
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 105
"""
"""
ANSWER-
"""
from bisect import bisect_right,bisect_left
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        words = set([word for word in words if word]) 
      
        nlens = sorted( set(map(len,words)) )
        def getsizes(L,i):

            if i:
                Lj = bisect_right(nlens,L) 
            else:
                Lj = bisect_left(nlens,L) 

            for j in range(Lj-1,-1,-1):
                yield nlens[j]

        def dfs(i,word,L):
            if i == L:
                return True

            for a in getsizes(L-i,i):
                if word[i:i+a] in words and dfs(i+a,word,L):
                    return True
            return False

        res = []
        for word in words:
            if dfs(0,word,len(word)):
                res.append(word)

        return res
"""
SOURCE-LEETCODE
"""