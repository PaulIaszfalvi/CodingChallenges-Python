class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        # Solutino 4
        nums.sort()        
        l = len(nums)//2
        end = len(nums)-1
        maximum = float('-inf')  # Initialize maximum outside the loop

        for i in range(l//2):
            pair_sum1 = nums[i] + nums[end-i]
            pair_sum2 = nums[l-1-i] + nums[l+i]
            maximum = max(maximum, pair_sum1, pair_sum2)

        return maximum

        # Solution 3 (Redone solution 1)
        # nums.sort()        
        # e = len(nums)-1
        # maximum = 0
        
        # for i in range(len(nums)//2):
        #     maximum = max(maximum, nums[i]+nums[e-i])

        # return maximum

        # Solution 2

        # nums.sort()        
        # l = len(nums)//2
        # maximum = nums[0] + nums[len(nums)-1]

        # print(nums)

        # for i in range(l):
        #     temp = nums[l-1-i] + nums[l+i]
        #     if temp < maximum:
        #         break
        #     maximum = temp

        # return maximum


        # Solution 1
        # nums.sort()        
        # e = len(nums)-1
        # maximum = 0
        
        # for i in range(e+1):
        #     maximum = max(maximum, nums[i]+nums[e-i])

        # return maximum

        # Online solution 
        # return nums.sort() or max(nums[i]+nums[-1-i] for i in range((len(nums)>>1)+1))