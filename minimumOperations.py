class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        count = 0
        l = len(nums)

        if l == len(set(nums)):
            return count

        while l > 0:
            nums = nums[3:]
            count += 1
            l -= 3

            if len(set(nums)) == l or l <= 0:
                return count

        
