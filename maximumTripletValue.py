class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        # Solution 2

        ans = 0
        max_num = nums[0]  # Maximum number seen so far
        max_diff = 0       # Maximum difference (nums[i] - nums[j]) seen so far
        
        for k in range(1, len(nums)):
            # Update answer using current number as k
            ans = max(ans, max_diff * nums[k])
            # Update max_diff using previous max_num and current number as j
            max_diff = max(max_diff, max_num - nums[k])
            # Update max_num
            max_num = max(max_num, nums[k])
            
        return ans

        # Solution 1

        ans = 0
        max_num = nums[0]  # Maximum number seen so far
        max_diff = 0       # Maximum difference (nums[i] - nums[j]) seen so far
        
        for k in range(1, len(nums)):
            # Update answer using current number as k
            ans = max(ans, max_diff * nums[k])
            # Update max_diff using previous max_num and current number as j
            max_diff = max(max_diff, max_num - nums[k])
            # Update max_num
            max_num = max(max_num, nums[k])
            
        return ans
