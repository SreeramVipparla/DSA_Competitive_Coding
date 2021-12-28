"""
QUESTION-

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
"""
"""
ANSWER-
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        i = 0
        while i < len(nums)-1 and nums[i] >= nums[i+1]:
            i += 1
        if i == len(nums) - 1:
            return num
        k = i
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[k]:
                k = j
        for j in range(i+1):
            if nums[j] < nums[k]:
                break
        nums[j], nums[k] = nums[k], nums[j]
        return int(''.join(nums))

"""
SOURCE-LEETCODE
"""