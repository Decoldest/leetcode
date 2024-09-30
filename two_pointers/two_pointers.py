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
    
    