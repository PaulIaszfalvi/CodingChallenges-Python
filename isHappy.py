class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set() 

        def get(n):
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)  
                n = list(str(n))
                ans = sum(int(x) ** 2 for x in n)
                return get(ans) 

        return get(n)