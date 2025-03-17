class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        # Solution 2

        d = Counter(nums)
        return all(count % 2 == 0 for count in d.values())

        # Solution 1
        
        l = len(nums)
        d = Counter(nums)

        if l % 2 != 0:
            return False

        for k in d:
            if d[k] % 2 != 0:
                return False

        return True
