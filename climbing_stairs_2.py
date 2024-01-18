class Solution:
    def climbStairs(self, n: int) -> int:       

        # Fibonacci Sequence

        f, s = 0, 1

        for x in range(n):
            f, s = s, s + f
        
        return s