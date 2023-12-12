class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Solution 2b 

        nums.sort()
              
        return (nums[-1]-1) * (nums[-2]-1)

        # Solution 2

        # nums.sort()
        # length = len(nums)
        
        # return (nums[length-1]-1) * (nums[length-2]-1)
        
        # Solution 1
        # first, second = nums[0], 0

        # for i in range(1, len(nums)):

        #     if nums[i] >= first:
        #         second = first
        #         first = nums[i]
        #     if nums[i] > second and nums[i] != first:
        #         second = nums[i]
        
        # return (first-1)*(second-1)