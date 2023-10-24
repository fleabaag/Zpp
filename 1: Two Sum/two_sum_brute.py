"""
Programa para resolver el problema #1
de LeetCode usando fuerza bruta (O(n^2)).
Author: @wallsified
Version: 1.0
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)): # i+1 evita usar el mismo indice en cada vuelta.
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
