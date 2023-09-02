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