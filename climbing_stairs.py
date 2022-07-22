class Solution:
    def climbStairs(self, n: int) -> int:
        
        fib_minus_two = 1
        fib_minus_one = 1
        
        if n == 1:
            return 1
                
        for i in range(1, n):
            
            fib = fib_minus_two + fib_minus_one
            
            fib_minus_two, fib_minus_one = fib_minus_one, fib
            
        return fib



    from functools import lru_cache
    @lru_cache(None)
    def climbStairs2(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    
sol = Solution();
print(sol.climbStairs(4))
print(sol.climbStairs2(4))
            

