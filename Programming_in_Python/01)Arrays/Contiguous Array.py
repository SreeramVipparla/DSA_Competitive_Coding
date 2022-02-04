"""
QUESTION-
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1
"""
"""
ANSWER-
"""

class Solution:
	def findMaxLength(self, nums: List[int]) -> int:
		count, maxi = 0, 0
		d = {0: -1}

		for i, j in enumerate(nums):
			if j == 0:
				count += -1
			else:
				count += 1

			try:
				temp = i - d[count]
				if maxi < temp:
					maxi = temp
			except:
				d[count] = i

		return maxi
"""
SOURCE-LEETCODE
"""