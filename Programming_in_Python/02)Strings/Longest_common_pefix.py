"""
QUESTION-

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
"""
ANSWER-
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
		
	
        column_slices, common_prefix = zip(*strs), ''
        
        for current_column in column_slices:
            
            if len(set(current_column)) == 1:
				
                common_prefix += current_column[0]
            
            else:
                break
                
        return common_prefix
"""
SOURCE-LEETCODE
"""
