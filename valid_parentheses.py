class ValidParentheses:

    def isValid(self, s:str) -> bool:

        stack = []       

        p_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for element in s:               
                       
                         
            if element in p_dict:                  
                stack.append(element)
               
            elif stack == [] or p_dict[stack.pop()] != element:        
                return False

        return stack == []
        
        # stack = []       

        # p_dict = {
        #     "]" : "[",
        #     ")" : "(",
        #     "}" : "{"
        # }

        # for element in s:        

        #     if element == "(" or element == "[" or element == "{":                
        #         stack.append(element)
        #     else:
        #         if stack == [] or stack.pop() is not p_dict[element]:                   
        #             return False

        # return stack == []


parentheses = "{}()[]{{([])}}"

test = ValidParentheses()
print(test.isValid(parentheses))

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []  # Create an empty stack to keep track of opening brackets
#         bracket_mapping = {')': '(', ']': '[', '}': '{'}  # Create a dictionary to map closing brackets to their corresponding opening brackets

#         for char in s:  # Iterate through each character in the input string
#             if char in bracket_mapping:  # If the character is a closing bracket
#                 top_element = stack.pop() if stack else '#'  # Pop the top element from the stack (or use '#' if the stack is empty)
#                 if bracket_mapping[char] != top_element:  # Check if the popped element matches the expected opening bracket
#                     return False  # If not, the sequence is invalid
#             else:
#                 stack.append(char)  # If the character is not a closing bracket, it's an opening bracket, so push it onto the stack

#         return not stack  # At the end, check if the stack is empty; if it is, the sequence is valid, otherwise, it's not
