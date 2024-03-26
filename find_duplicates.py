class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # Solution 2

        seen = set()
        duplicates = set()
        
        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        return list(duplicates)

        # Solution 1
        
        d = {}

        for x in nums:
            d[x] = d.get(x, 0) + 1

        ans = []

        for x in d:

            if d.get(x) > 1: 
                ans.append(x)

        return ans