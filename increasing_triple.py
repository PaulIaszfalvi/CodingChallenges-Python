class Solution:
    def increasingTriplet(self, nums) -> bool:


        # Solution 1
        # count, minimum = 0, nums[0]

        # for i in nums:
        #     print("start", minimum, i)
        #     if minimum < i:
        #         minimum = i              
        #         count += 1

        #     minimum = min(i,minimum)
        #     print("end", minimum, i)
        
        # return count >= 2

        # Solution 2

        # first, second, third = float('inf'), float('inf'), float('inf')

        # for i in nums:
        #     if i < first:
        #         first = i
        #     elif i < second:
        #         second = i
        #     else:
        #         return True
        # return False

        # Working Solution 

        first, second = float('inf'), float('inf')
        
        for third in nums:
            
            if second < third: return True
            if third <= first: first= third    
            else:  second = third 
                
        return  False
    

nums = [1,2,3,4,5]
#print(Solution().increasingTriplet(nums))
nums = [5,4,3,2,1]
#print(Solution().increasingTriplet(nums))
nums = [2,1,5,0,4,6]
print(Solution().increasingTriplet(nums))
nums =[0,4,2,1,0,-1,-3]
#print(Solution().increasingTriplet(nums))