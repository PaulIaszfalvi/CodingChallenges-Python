class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # Solution 2

        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            current_sum = left * left + right * right
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        
        return False

        # Solution 1

        c_s = c**2
        l = {x**2 for x in range(c+1)}

        for x in l:            
            if c_s - x in l:
                return True

        return False
