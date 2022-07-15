class Solution(object):
    def search(self, nums, target):
        
        midIndex = len(nums)/2
        leftIndex = 0
        rightIndex = len(nums)-1
    
        while(leftIndex <= rightIndex):
                   
            if nums[midIndex] < target:
                leftIndex = midIndex + 1
            elif nums[midIndex] > target:
                rightIndex = midIndex - 1
            else: 
                return midIndex
               
            midIndex = (leftIndex + rightIndex)/2
            
        
        return -1