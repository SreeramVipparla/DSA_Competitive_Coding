"""
QUESTION-

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""
"""
ANSWER-
"""
def Wildcard_Matching(self, s, p):
    sn, pn = len(s), len(p)
    si = pi = 0
    save_si, save_pi = None, None
    while si < sn:
        if pi < pn and (p[pi] == '?' or p[pi] == s[si]):
            si += 1
            pi += 1
        elif pi < pn and p[pi] == '*':
            # Meet "*", save si and pi, searching for next character
            save_si, save_pi = si + 1, pi
            pi += 1
        elif save_pi is not None:
            # Dead end, restore si and pi, carry on.
            si, pi = save_si, save_pi
        else:
            return False
    return p[pi:].count("*") == pn - pi
"""
SOURCE-LEETCODE
"""