class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        result = []
        carry = 0        
        a = list(a)
        b = list(b)
        length_a = len(a)
        length_b = len(b)      
        max_length = length_a if length_a > length_b else length_b        
        
        while max_length >= 0 or carry == 1:     
         
            max_length -= 1
            length_a -= 1
            length_b -= 1
            
            placeholder_a = a[length_a] if length_a >= 0 else '0'
            placeholder_b = b[length_b] if length_b >= 0 else '0'
                         
            temporary = int(placeholder_a) + int(placeholder_b)
            
            if temporary > 1:
                if carry == 1:
                    result = ['1'] + result
                    carry = 0
                else:
                    carry = 1
                    result = ['0'] + result
            elif temporary == 1:
                if carry == 1:
                    result = ['0'] + result                 
                else: 
                    result = [str(temporary)] + result
            else:
                if carry == 1:
                    result = ['1'] + result
                    carry = 0
                else:
                    result = ['0'] + result 
                        
        if carry == 1:
            result = ['1'] + result
            
        return "".join(result)