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

      
