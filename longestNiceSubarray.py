from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        window_mask = 0
        max_length = 0

        for right in range(len(nums)):
            # If adding nums[right] causes a conflict, shrink the window
            while (window_mask & nums[right]) != 0:
                window_mask ^= nums[left]  # Remove leftmost element from the window
                left += 1
            
            # Add nums[right] to the window
            window_mask |= nums[right]
            
            # Update the maximum length of the nice subarray
            max_length = max(max_length, right - left + 1)

        return max_length
