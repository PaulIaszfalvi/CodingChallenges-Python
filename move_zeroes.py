from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # for e in nums[::-1]:
        #     print(e)
        
        iter_zero = len(nums) - 1
        iter_num = len(nums) - 2
        

        while iter_num >= 0:

            if nums[iter_zero] is not 0:
                iter_zero -= 1
            elif nums[iter_num] is 0:
                iter_num -= 1
            else:
                nums[iter_zero], nums[iter_num] = nums[iter_num], nums[iter_zero]
                iter_zero -= 1

        print(nums)   
            
        

nums = [0,1,72,3,0,5,9,0,6,51,0,3]
nums_2 = [0,0,1,2,3,0,0,4,5,6,0,7,0,0,8,0,9,0]
sol = Solution()
sol.moveZeroes(nums)
sol.moveZeroes(nums_2)