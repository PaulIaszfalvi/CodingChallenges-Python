class Solution(object):
    def runningSum(self, nums):
        
        sum = 0
        
        for index, element in enumerate(nums): 
            sum =  sum + element
            nums[index] = sum
        
        return nums

print(Solution().runningSum([1,2,3,4,5,6]))