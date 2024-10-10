# Validate Parentheses
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
        

      
