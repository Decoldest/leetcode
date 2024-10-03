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
    
# Longest Substring Witohut Duplicates
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