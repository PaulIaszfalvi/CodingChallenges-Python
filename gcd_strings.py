class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        divisor = ""

        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                divisor += str1[i]
            else:
                divisor = ""
                break     

            if len(str1) % len(divisor) == 0 and len(str2) % len(divisor) == 0:

                    multiple1 = len(str1) / len(divisor)
                    multiple2 = len(str2) / len(divisor)
                    
                    if divisor * multiple1 == str1 and divisor * multiple2 == str2:
                        break

       
        
        return divisor

        