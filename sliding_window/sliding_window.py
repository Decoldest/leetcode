from collections import defaultdict, Counter
from typing import List

# Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min = prices[0]

        for price in prices:
            curr = price
            if min > curr:
                min = curr
            result = max(result, curr - min)
        
        return result
    
# Longest Substring Without Duplicates
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, start = 0, 0
        currentSet = set()

        for r in range(len(s)):
            letter = s[r]

            while letter in currentSet:
                currentSet.remove(s[start])
                start += 1

            currentSet.add(letter)
            result = max(result, r - start + 1)
        return result
    

# Longest Repeating Substring With Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left, result = 0, 0

        for i in range(len(s)):
            count[s[i]] += 1

            while(i - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, i - left + 1)

        return result
    
# Permutation String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      lengthSmaller, lengthLarger = len(s1), len(s2)

      if lengthLarger < lengthSmaller:
        return False

      frequencies, used = Counter(s1), Counter(s2[:lengthSmaller])

      for i in range(lengthSmaller, lengthLarger):
        if used == frequencies:
          return True

        used[s2[i]] += 1

        used[s2[i - lengthSmaller]] -= 1

      return used == frequencies