class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero = False

        for e in nums:
            if e == 0:
                zero = True
            else:
                product *= e

        for i, v in enumerate(nums):
          
            if v != 0 and zero:
                nums[i] = 0
            elif v == 0:
                nums[i] = int(product)                
            elif v == 0 and zero:
                nums[i] = 0            
            else: 
                nums[i] = product // v

        return nums

