class Solution:
    def maxOperations(self, nums, k: int) -> int:
        
        # Solution 1
        # complements = []
        # b = f = pairs = 0
        

        # if len(nums) < 2:
        #     return 0

        # while f < len(nums)-1:
          
        #     b = f + 1            
        #     while b < len(nums):                
        #         if nums[b] == k - nums[f]:
        #             pairs += 1
                   
        #             nums.pop(b)
        #             break
        #         b += 1            
           
        #     f += 1
      
        # return pairs
        
        # Solution 2 
        # 
        cache = {}
        num_ops = 0
        for i in nums:
            if cache[i] > 0:
                cache[i] -= 1
                num_ops += 1
                continue
            cache[k-i] += 1
        return num_ops   

nums = [1,2,3,4]
k = 5
print(Solution().maxOperations(nums, k))

nums = [3,1,3,4,3]
k = 6
print(Solution().maxOperations(nums, k))