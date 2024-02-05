class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base, exponent):
            if exponent == 0:
                return 1
            if exponent < 0:
                return 1 / helper(base, -exponent)
            result = helper(base, exponent // 2)
            return result * result if exponent % 2 == 0 else result * result * base

        return helper(x, n)
    
print(Solution().myPow(5,333))