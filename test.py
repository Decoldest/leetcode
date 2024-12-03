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



class Matrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow, bottomRow = 0, len(matrix) - 1

        while(topRow <= bottomRow):
            middleRow = (topRow + bottomRow) // 2
            
            if(matrix[middleRow][0] > target):
                bottomRow = middleRow - 1
                print("too big")
            elif(matrix[middleRow][-1] < target):
                topRow = middleRow + 1
                print("too small")
            else:
                print("break")
                break
        
        
        currentRow = matrix[middleRow]
        left, right = 0, len(currentRow) - 1

        print(currentRow)

        while(left <= right):
            middle = (left + right) // 2
            currentNumber = currentRow[middle]
            # print("currentNUm: ", currentNumber)

            if(currentNumber > target):
                right = middle - 1
            elif(currentNumber < target):
                left = middle + 1
            else:
                return True
            
        return False 
        
mat = Matrix()
mat.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)