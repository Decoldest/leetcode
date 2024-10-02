from typing import List

# Is Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        letters = s.lower()

        while start < end:
            if letters[start] == " " or not letters[start].isalnum():
                start += 1
                continue
            if letters[end] == " " or not letters[end].isalnum():
                end -= 1
                continue

            if letters[start] != letters[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
    
# Two Integer Sum II
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            current = numbers[start] + numbers[end]
            if current > target:
                end -= 1
            elif current < target:
                start += 1
            else:
                return [start + 1, end + 1]
            
# Three Integer Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, current in enumerate(nums):
            if current > 0:
                break
            if index > 0 and current == nums[index - 1]:
                continue

            middle, third = index + 1, len(nums) - 1

            while middle < third:
                numSum = current + nums[middle] + nums[third]
                if numSum > 0:
                    third -= 1
                elif numSum < 0:
                    middle += 1
                else:
                    result.append([current, nums[middle], nums[third]])
                    middle += 1
                    third -= 1
                    while nums[middle] == nums[middle - 1] and middle < third:
                        middle += 1


        return result

# Max Water Container
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1

        while right > left:
            leftHeight, rightHeight = heights[left], heights[right]
            area = (right - left) * min(leftHeight, rightHeight)

            result = max(area, result) 

            if leftHeight >= rightHeight:
                right -= 1
            else: 
                left += 1

        return result

        