class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Solution 1

        if not nums:
            return 0

        # Initialize an array to store LIS ending at each index
        arr = [[] for _ in range(len(nums))]

        # Base case: LIS at each index is at least one and different (otherwise we generate the same list over)
        for i in range(len(nums)):
            arr[i].append(nums[i])

        # Iterate through each element in nums
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and len(arr[i]) < len(arr[j]) + 1:
                    arr[i] = arr[j] + [nums[i]]

        return max(len(x) for x in arr)
    
        # Faster online solution 
    
        # if not nums:
        #     return 0
        
        # n = len(nums)
        # dp = [1] * n

        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)
    
        # Online beast solution 
    
        # arr = [nums.pop(0)]                  # <-- 1) initial step
 
        # for n in nums:                       # <-- 2) iterate through nums
            
        #     if n > arr[-1]:                  # <--    2a)
        #         arr.append(n)

        #     else:                            # <--    2b)
        #         arr[bisect_left(arr, n)] = n 

        # return len(arr)    