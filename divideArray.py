class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        l = len(nums)
        d = Counter(nums)

        if l % 2 != 0:
            return False

        for k in d:
            if d[k] % 2 != 0:
                return False

        return True
