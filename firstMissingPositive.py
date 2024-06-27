class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        ma = 0
        mi = 0
        d = {}

        for x in nums:
            d[x] = d.get(x, 0) + 1
            if x > 0:
                ma = max(ma, x)
                mi = min(mi, x)

        for x in range(mi - 1, ma + 2):          
            if x not in d and x > 0:
                return x
