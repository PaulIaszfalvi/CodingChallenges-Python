class Solution:
    def numDecodings(self, s: str) -> int:
        
        # # Solution 1

        # if '0' == s[0]:
        #         return 0

        # if len(s) == 1:
        #     return 1

        # result = 1  

        # for i in range(1, len(s)): 
        #     two_digit = int(s[i-1:i+1])

        #     if 10 <= two_digit <= 26:
        #         result += 1

        #     if s[i] != '0':
        #         result += 1

        # return result

        # # Solution 1 prototype
        # if '0' == s[0]:
        #     return 0

        # if len(s) == 1:
        #     return 1

        # result = 0

        # for i in range(len(s)-1):
           
        #     if int(s[i:i+2]) <= 26:
        #         result += 1
        #     if int(s[i]) != 0 and int(s[i+1])!= 0:
        #         result += 1
            

        # return result