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