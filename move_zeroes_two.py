class Solution:
    def moveZeroes(self, nums):
        

        # if len(nums) == 0:
        #     return nums

        # left = 0
        # right = len(nums)-1

        # while left < right:
            
        #     while nums[right] != 0 and right > left:
        #         right -= 1

        #     while nums[left] == 0:
        #         left += 1
          
        #     nums[right], nums[left] = nums[left], nums[right]

        #Quick and easy   
        # zeros = [x for x in nums if x == 0]
        # non_zeros = [x for x in nums if x != 0]
        
        # return zeros + non_zeros

        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            if nums[slow] != 0:
                slow += 1

        return nums
        
nums = [0,1,0,3,12,0]
print(Solution().moveZeroes(nums))





