class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Solution 2 (Bitwise and operation)
        if n <= 0:
            return False
        return n & (n - 1) == 0

        # Solution 1

        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2  
        return True
