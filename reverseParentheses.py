class Solution:
    def reverseParentheses(self, s: str) -> str:
        
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
