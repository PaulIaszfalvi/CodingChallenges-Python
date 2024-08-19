class Solution:
    def minSteps(self, n: int) -> int:
        def get_prime_factors(x):
            factors = []
            # Check for number of 2s
            while x % 2 == 0:
                factors.append(2)
                x //= 2
            # Check for odd factors from 3 onwards
            factor = 3
            while factor * factor <= x:
                while x % factor == 0:
                    factors.append(factor)
                    x //= factor
                factor += 2
            if x > 2:
                factors.append(x)
            return factors
        
        if n == 1:
            return 0
        
        prime_factors = get_prime_factors(n)
        return sum(prime_factors)
