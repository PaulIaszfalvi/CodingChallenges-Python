class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Solution 1
        
        d = {}

        for x in nums:
            d[x] = d.get(x, 0) + 1

            if d[x] > 1:
                return x
        