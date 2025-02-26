class Solution:
    def reverse(self, x: int) -> int:
        
        isNegative = x < 0
        x = abs(x)
        ans = ""

        if x == 0:
            return 0

        while x > 0:
            ans += str(x % 10) 
            x //= 10

        ans = int(ans)

        if ans < -2**31 or ans > 2**31 - 1:
            return 0  

        return ans * (-1 if isNegative else 1) 

        
