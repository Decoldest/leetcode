## Array questions in Leetcode 150
from typing import List

# Duplicate Integer
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
# Is Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
# Two Integer Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in seen:
                return [seen[difference], i]
            seen[n] = i