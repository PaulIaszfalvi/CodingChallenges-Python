class Solution:
    def maximumCount(self, nums: List[int]) -> int:

      # Optimized python 
        neg_count = bisect.bisect_left(nums, 0)  # First index of 0 (or first positive number)
        pos_count = len(nums) - bisect.bisect_right(nums, 0)  # Count of positive numbers

        return max(neg_count, pos_count)

      # Solution 2 Binary Search

    def binSrch(self, nums: List[int], target: int) -> int:
        """Binary search to find the first occurrence of target (or where it should be inserted)."""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1  # Move right to find first occurrence of target
            else:
                right = mid - 1  # Move left to narrow down first occurrence
        return left  # Returns the index of the first occurrence of target
    
    def maximumCount(self, nums: List[int]) -> int:
        """Finds the maximum count of either negative or positive numbers."""
        neg_count = self.binSrch(nums, 0)  # Count of negative numbers
        pos_count = len(nums) - self.binSrch(nums, 1)  # Count of positive numbers

        return max(neg_count, pos_count)

      # Solution 1
        
        idx1 = 0
        idx2 = len(nums) - 1

        for i, v in enumerate(nums):
            if v > 0:
                idx2 = i
                break
            if v < 0:
                idx1 = i

        pos = len(nums) - idx2 

        if idx1 == 0 and idx2 == len(nums) - 1 and nums[0] == 0:
            return 0

        return max(idx1 + 1, pos) 
