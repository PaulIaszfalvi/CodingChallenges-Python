class Solution:
    def productExceptSelf(self, nums):

        product = 1
        zeroes = 0

        for x in nums:
            if x == 0:
                zeroes += 1
            else:
                product *= x
        if zeroes > 1:
            return [0] * len(nums)

        for i, x in enumerate(nums):
            
            if x != 0 and zeroes < 1:
                nums[i] = product // x            
            elif x == 0 and zeroes == 1:
                nums[i] = product
            else:
                nums[i] = 0
               

        return nums





        
        # product = 1
        # zero = False

        # for e in nums:
        #     if e == 0:
        #         zero = True
        #     else:
        #         product *= e

        # for i, v in enumerate(nums):
          
        #     if v != 0 and zero:
        #         nums[i] = 0
        #     elif v == 0:
        #         nums[i] = int(product)                
        #     elif v == 0 and zero:
        #         nums[i] = 0            
        #     else: 
        #         nums[i] = product // v

        # return nums
        

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))