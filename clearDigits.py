class Solution:
    def clearDigits(self, s: str) -> str:

      # Solution 2

      stack = []

        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


      # Solution 1

        key = "abcdefghijklmnopqrstuvwxyz"
        
        stack = []

        for char in s:
            if char not in key:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
