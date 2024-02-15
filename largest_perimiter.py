class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        # Solution 2

        nums.sort()
        s = sum(nums)
        n = len(nums)
       
        for x in nums[n-1:0:-1]:
            s -= x
            if s > x:
                return s + x
        return -1

        # Solution 1 (Attempt fail test cases)
        nums.sort()

        ans = 0
        c = 0

        if len(nums) == 3:
            if sum(nums[0:2]) <= nums[-1]:
                return -1
       
        print(nums)

        for x in nums:  

            if c >= 3 and ans <= x:
                print(c, x)
                return ans 
            elif c < 3 and 0 < ans < x:            
                return -1   

            c += 1  
            ans += x      
              
        return ans
        