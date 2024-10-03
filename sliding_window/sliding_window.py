# Buy and Sell Crypto
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