class Solution:
    def findMaxAverage(self, nums, k) -> float:
     
        result = maxResult = sum(nums[:k])
        
        for i in range(k, len(nums)):
                       
            result += nums[i] - nums[i-k]
                       
            if result > maxResult:
                maxResult = result
            
        return maxResult/k
    

nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))