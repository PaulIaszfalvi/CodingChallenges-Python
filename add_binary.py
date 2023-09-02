import itertools

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        result = ''
        carry = 0

        a = a[::-1]
        b = b[::-1]

        for pair in itertools.zip_longest( a, b):
                      
            if pair[0] is not None and pair[1] is not None:
                temp = int(pair[0]) + int(pair[1])
            else:
                temp = int(pair[0]) if pair[0] is not None else int(pair[1])
           
            placeholder = (carry + temp) 
            iter_result = placeholder % 2            
            carry = placeholder // 2

            result += str(iter_result)

        if carry:
            result += str(carry)

        return result[::-1]
       #

       

        # result = []
        # carry = 0        
        # a = list(a)
        # b = list(b)
        # length_a = len(a)
        # length_b = len(b)      
        # max_length = length_a if length_a > length_b else length_b        
        
        # while max_length >= 0:     
         
        #     max_length -= 1
        #     length_a -= 1
        #     length_b -= 1
            
        #     placeholder_a = a[length_a] if length_a >= 0 else '0'
        #     placeholder_b = b[length_b] if length_b >= 0 else '0'
                         
        #     temporary = int(placeholder_a) + int(placeholder_b)
            
        #     if temporary > 1:
        #         if carry == 1:
        #             result = ['1'] + result
        #             carry = 0
        #         else:
        #             carry = 1
        #             result = ['0'] + result
        #     elif temporary == 1:
        #         if carry == 1:
        #             result = ['0'] + result                 
        #         else: 
        #             result = [str(temporary)] + result
        #     else:
        #         if carry == 1:
        #             result = ['1'] + result
        #             carry = 0
        #         else:
        #             result = ['0'] + result 
                        
        # if carry == 1:
        #     result = ['1'] + result
            
        # return "".join(result)
a = ['1', '1']
b = ['1']

sol = Solution()
print(sol.addBinary(a, b))