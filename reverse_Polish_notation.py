class Solution:
    def evalRPN(self, tokens):

        # Solution 2
        stack = []
                                                            
        for t in tokens:                                    
            if t not in '/+-*':                                
                stack.append(int(t))                          
                                                               
            else:                                              
                num = stack.pop()                             
                if   t == '+': stack[-1]+=  num
                elif t == '-': stack[-1]-=  num
                elif t == '*': stack[-1]*=  num
                else         : stack[-1]= int(stack[-1]/num)    

        return stack[0]


        # # Solution 1
        # op = "+-*/"
        # stack = []
        # result = 0

        # for x in tokens:                  
        #     if x in op:        
        #         print(x, stack)            
        #         val2 = stack.pop()
        #         val1 = stack.pop()
        #         if x == "+":
        #             result = val1 + val2
        #         elif x == "-":
        #             result = val1 - val2
        #         elif x == "*":
        #             result = val1 * val2
        #         else:   
        #             result = int(val1 / val2)
        #         stack.append(result)
        #     else:
        #         stack.append(int(x))

        # return stack[-1]

tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))