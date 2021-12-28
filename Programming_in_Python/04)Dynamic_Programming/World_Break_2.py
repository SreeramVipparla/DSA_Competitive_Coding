"""
QUESTION-

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""
"""
ANSWER-
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.dfs(s, set(wordDict), {})
    
    def dfs(self, s, d, m):
        if s in m: # memorize
            return m[s]
        if not s:
            return [""]
        res = []
        for i in range(1, len(s)+1):
            if s[:i] in d:
                for word in self.dfs(s[i:], d, m):
                    res.append(s[:i] + (" " if word else "") + word)
        m[s] = res
        return res
    
    def wordBreak1(self, s, wordDict):
        res = []
        self.dfs(s, set(wordDict), "", res)
        return res
    
    def dfs1(self, s, dic, path, res):
        if self.check(s, dic):
            if not s:
                res.append(path[1:])
            for i in range(1, len(s)+1):
                if s[:i] in d:
                    self.dfs(s[i:], dic, path+" "+s[:i], res)
                
    def check(self, s, dic):
        dp = [False] * (1+len(s))
        dp[0] = True
        for j in range(1, len(s)+1):
            for i in range(j):
                if dp[i] and s[i:j] in dic:
                    dp[j] = True
                    break
        return dp[-1]
"""
SOURCE-LEETCODE
"""