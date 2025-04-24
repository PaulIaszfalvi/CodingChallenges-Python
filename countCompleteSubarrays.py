from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        x = len(set(nums))  # Number of distinct elements
        count = 0
        freq = Counter()  # Track frequencies in window
        l = 0
        
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while len(freq) == x:  # Window has all distinct elements
                count += len(nums) - r  # Count subarrays ending at r
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
        
        return count
