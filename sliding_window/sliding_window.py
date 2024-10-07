from collections import defaultdict
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