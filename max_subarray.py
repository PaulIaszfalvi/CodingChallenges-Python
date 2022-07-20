class Solution(object):
    def maxSubArray(self, nums):
      
        max_sum = nums[0]
        cur_sum = 0
        
        for i in range(len(nums)):            
            
            cur_sum += nums[i]
            
            if max_sum < cur_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum

sol = Solution()
print(sol.maxSubArray([1,2,3,4,-5,-6,2]))