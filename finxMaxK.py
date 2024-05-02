class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        # Solution 3

        num_set = set(nums)
        max_k = -1

        for x in num_set:
            if -x in num_set:
                max_k = max(max_k, abs(x))

        return max_k

        # Solution 2

        d = {}
        m = -1

        for x in nums:
            d[x] = d.get(x, 0) + 1

        for x in d.keys(): 
            if -x in d: 
                m = max(abs(x), m)
                
        return m


        # Solution 1
        
        d = {}
        m = -1

        for x in nums:
            d[x] = d.get(x, 0) + 1

        for x in d.items():
           
            if d.get(-1 * x[0]):
                m = max(abs(x[0]), m)
                
        return m