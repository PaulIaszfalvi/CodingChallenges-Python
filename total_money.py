class Solution:
    def totalMoney(self, n: int) -> int:
        
        a = n // 7
        b = n % 7
        return int(7*((a*(a+1)/2) + 3 * a) + (b*(b+1)/2)) + a*b