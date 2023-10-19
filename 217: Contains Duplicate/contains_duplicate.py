"""
Solución al problema 217 de Leetcode
Author: @wallsified
Version: 1.0

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
