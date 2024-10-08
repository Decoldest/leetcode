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
    
sol = Solution()
s1 = "adc"
s2 = "dcda"
print(sol.checkInclusion(s1, s2))