class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

      # Solution 2

      if any(num < k for num in nums):
            return -1
        
        values_above_k = set(num for num in nums if num > k)
        
        if not values_above_k:
            return 0
        
        return len(values_above_k)


      # Solution 1
        
        d = set(nums)
        ans = 0

        if len(d) == 1 and k in d:
            return ans

        for i in d:
   
            if i > k:
                ans += 1

        return -1 if ans == 0 else ans
