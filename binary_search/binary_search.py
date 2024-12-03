
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
    
# Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow, bottomRow = 0, len(matrix) - 1

        while(topRow <= bottomRow):

            middleRow = (topRow + bottomRow) // 2
            
            if(matrix[middleRow][0] > target):
                bottomRow = middleRow - 1
            elif(matrix[middleRow][-1] < target):
                topRow = middleRow + 1
            else:
                break
        
        
        currentRow = matrix[middleRow]
        left, right = 0, len(currentRow) - 1

        while(left <= right):
            middle = (left + right) // 2
            currentNumber = currentRow[middle]

            if(currentNumber > target):
                right = middle - 1
            elif(currentNumber < target):
                left = middle + 1
            else:
                return True
            
        return False 