from collections import Counter

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
    
class Stack:
  def isValid(self, s: str) -> bool:

    stack = []
    characterMap = { 
        ")" : "(",
        "]" : "[",
        "}" : "{",
    }

    for char in s:
      if not char in characterMap:
        stack.append(char)
      else: 
        if not stack or characterMap[char] != stack.pop():
          return False        

    return not stack
  
stackSolution = Stack()
s="[(])"
print(stackSolution.isValid(s))

