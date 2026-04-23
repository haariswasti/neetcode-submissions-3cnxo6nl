class Solution:
    def isValid(self, s: str) -> bool:
      
      
      stack = []
      store = {')': '(', ']': '[', '}':'{'}

      for i in s:
        if i in store:
            if not stack or stack[-1] != store[i]:
                return False
            stack.pop()
        else:
            stack.append(i)
      return len(stack) == 0
        