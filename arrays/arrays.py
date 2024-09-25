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
              
# String Encode and Decode
class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "*" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = s.find("*")

        while(index > -1):
            length = int(s[:index])
            result.append(s[index + 1 : index + 1 + length])
            s = s[index + 1 + length:]
            index = s.find("*")

        return result

# Product of array discluding self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            result[i] = prefix
            prefix *= nums[i]
      
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

# Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for i in range(9)]
        subBox = defaultdict(set)

        for i, row in enumerate(board):
            rowNums = set()
            for j, digit in enumerate(row):
                if digit == ".":
                    continue

                if digit in rowNums:
                    return False
                rowNums.add(digit)

                if digit in col[j]:
                    return False
                col[j].add(digit)

                if digit in subBox[(i // 3, j // 3)]:
                    return False
                subBox[(i // 3, j // 3)].add(digit)

        return True

# Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        result = 0

        for num in values:
            if num - 1 not in values:
                length = 1
                j = 1
                while num + j in values:
                    length += 1
                    j += 1

                if length > result:
                    result = length
        
        return result

