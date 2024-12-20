# Validate Parentheses
from typing import List


class Solution:
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

# Minimum Stack
class MinStack:
  def __init__(self):
    self.stack = []
    self.minimumStack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    if self.minimumStack:
      val = min(val, self.minimumStack[-1])
    self.minimumStack.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.minimumStack.pop()

      
  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minimumStack[-1]
        
# Evaluate Reverse Polish Notation
class Solution:
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

      
# Generate Parenthesis
class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
      
    stack = []
    result = []

    def recursive(openBracketsN, closedBracketsN):
      if openBracketsN == closedBracketsN == n:
        result.append("".join(stack))
        return
      
      if openBracketsN < n:
        stack.append("(")
        recursive(openBracketsN + 1, closedBracketsN)
        stack.pop()

      if closedBracketsN < openBracketsN:
        stack.append(")")
        recursive(openBracketsN, closedBracketsN + 1)
        stack.pop()
      
    recursive(0,0)
    return result 

# Daily Temperatures
class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []

    for (i, temperature) in enumerate(temperatures):
      while stack and temperature > stack[-1][1]:
        poppedIndex, poppedTemp = stack.pop()
        result[poppedIndex] = (i - poppedIndex)
      stack.append([i, temperature])
    return result