class Solution:
    def longestSubarray(self, nums) -> int:
      
        ans = sum = lo = 0

        for hi, num in enumerate(nums):
            sum += num
            if sum < hi - lo:
                sum -= nums[lo]
                lo += 1
            ans = max(ans, hi - lo)
            
        return ans





nums = [1,1,0,1]
print(Solution().longestSubarray(nums))
nums = [0,1,1,1,0,1,1,0,1]
print(Solution().longestSubarray(nums))
nums = [1,1,1]
print(Solution().longestSubarray(nums))