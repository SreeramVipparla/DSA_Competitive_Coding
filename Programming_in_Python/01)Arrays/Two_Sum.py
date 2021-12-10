"""
QUESTION-

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""
"""
ANSWER-
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement ={}
        for i,v in enumerate(nums):
            # if v = nums[i] in complement, we find a solution
            if v in complement:
                return complement[v],i
            # if v = nums[i] not in complement, we store the compliment of the element into the dictionary.
            else:
                complement[target - v] = i
        return -1

"""
SOURCE-LEETCODE
"""