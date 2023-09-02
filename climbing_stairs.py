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

    def climbStairs2(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs2(n-1) + self.climbStairs2(n-2)
    
    
sol = Solution();
print(sol.climbStairs(24))
print(sol.climbStairs2(24))
            

