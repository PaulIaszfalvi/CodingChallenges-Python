class Solution:
    def reverseParentheses(self, s: str) -> str:

        # Solution 2

        stack = []
        
        for char in s:
            if char == ')':
                # Extract the substring inside the parentheses and reverse it
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  # Remove the opening parenthesis '('
                stack.extend(temp)  # Push the reversed substring back onto the stack
            else:
                stack.append(char)
        
        return ''.join(stack)

        # Solution 1
        
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters from the stack until an opening parenthesis is found
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                # Pop the opening parenthesis '('
                stack.pop()
                
                # Push the reversed content back onto the stack
                stack.extend(temp)
            else:
                # Push current character onto the stack
                stack.append(char)
        
        # Join the characters to form the final result
        return ''.join(stack)
