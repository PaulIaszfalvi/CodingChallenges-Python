class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(arith, x, y):
            match arith:
                case '+':
                    return x + y
                case '-':
                    return y - x
                case '*':
                    return x * y
                case '/':                   
                    return int(y / x)

        stack = []
        arith = "*/+-"      

        for x in tokens:
            if x not in arith:
                stack.append(int(x))
            else:
                ans = calc(x, stack.pop(), stack.pop())
                stack.append(ans)           
        
        return stack[-1]
    
    