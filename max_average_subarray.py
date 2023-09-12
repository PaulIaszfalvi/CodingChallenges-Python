class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
     
        result = maxResult = sum(nums[:k])

        for i in range(k, len(nums)):
                       
            result += nums[i] - nums[i-k]
                       
            if result > maxResult:
                maxResult = result
            
        return maxResult/k