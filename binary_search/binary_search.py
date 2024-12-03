
from typing import List

# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while(left <= right):
            middle = (left + right) // 2
            current = nums[middle]
            # Too high, go to first half
            if(current > target):
                right = middle - 1
            # Too low, go to second half
            elif(current < target):
                left = middle + 1
            else:
                return middle

        return -1