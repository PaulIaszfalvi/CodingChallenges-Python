class Solution:
    def longestOnes(self, nums, k: int) -> int:
        
        # Solution 1

        # front, back, result = 0

        # if len(nums) <= k:
        #     return k

        # while back < len(nums) and front < len(nums)-1:
        #     if nums[back] == 1 or k > 0:
        #         if nums[back] == 0:
        #             k -= 1
        #         back += 1 
                         
        #     else:                 
        #         if nums[front] == 0:
        #             k += 1
        #         front += 1
        #     result = max(result, back-front)
            
        # return result

        # Solution 2

        # Go through the loop once, the front and back counter will get stuck on the biggest solution 
        # return the biggest solution by subtracting the indexes of front and back
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution().longestOnes(nums, k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(Solution().longestOnes(nums, k))

nums = [0,0,0,1]
k = 4
print(Solution().longestOnes(nums, k))