from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        valid_operators = {'+', '-', '*', '/'}
        numbers_stack = []

        for e in tokens:

            if e in valid_operators:
                second = numbers_stack.pop()
                first = numbers_stack.pop()
                
                result = self.calc(first, second, e)
             
                numbers_stack.append(result)
               
            else:
                numbers_stack.append(int(e))
                
        return numbers_stack.pop()

    def calc(self, x, y, operator):
        match operator:
            case '+':
                return x + y
            case '-':
                return x - y
            case '*':
                return x * y  
            case '/':
                return int(x / y)

sol = Solution()

tokens = ["2","1","+","3","*"]
print(sol.evalRPN(tokens))
tokens = ["4","13","5","/","+"]
print(sol.evalRPN(tokens))
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))

# Cool Solution 

# self.operators = {
#             '+': lambda y, x: x + y,
#             '-': lambda y, x: x - y,
#             '*': lambda y, x: x * y,
#             '/': lambda y, x: int(operator.truediv(x, y))
#         }

#     def evalRPN(self, tokens):
#         if not tokens:
#             return 0

#         stack = []

#         for token in tokens:
#             if token in self.operators:
#                 stack.append(self.operators[token](stack.pop(), stack.pop()))
#             else:
#                 stack.append(int(token))

#         return stack[0]