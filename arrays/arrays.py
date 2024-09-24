## Array questions in Leetcode 150
from collections import defaultdict
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

# Anagram Groups
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            letters = "".join(sorted(word))
            if letters in anagrams:
                anagrams[letters].append(word)
            else:
                anagrams[letters] = [word]

        return anagrams.values()

# Top K Elements in List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
          counts[num] += 1;

        frequency = [[] for i in range(len(nums) + 1)] 

        for number, count in counts.items():
          frequency[count].append(number)

        result = []
        
        for value in range(len(frequency) - 1, 0, -1):
          for fr in frequency[value]:
              result.append(fr)
              if(len(result) == k):
                  return result