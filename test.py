from collections import Counter
from typing import List

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


class Operator:
  def operate(self, first, second, operator) -> int:
    result = 0
    if(operator == "+"):
      result = first + second
    elif(operator == "-"):
      result = first - second
    elif(operator == "*"):
      result = first * second
    else:
      result = int(float(first / second))
    return result

  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for string in tokens:
      if not string  in ["+", "-", "*", "/"]:
        stack.append(int(string))

      else:
        second = stack.pop()
        first = stack.pop()
        
        stack.append(self.operate(first, second, string))
    return stack.pop()



sol = Operator()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))

        