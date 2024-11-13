from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        # Faster online solution

        v.sort()
        ans = 0
        for i in range(len(v) - 1):
            low = bisect_left(v, lower - v[i], i + 1)
            up = bisect_right(v, upper - v[i], i + 1)
            ans += up - low
        return ans


        # Solution 1

        # Sort the list in place
        nums.sort()
        ans = 0
        n = len(nums)

        # Two pointers to find fair pairs
        for i in range(n - 1):
            left = i + 1
            right = n - 1

            # Find the smallest index `left` where nums[i] + nums[left] >= lower
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] < lower:
                    left = mid + 1
                else:
                    right = mid - 1

            # Find the largest index `right` where nums[i] + nums[right] <= upper
            low = left
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[i] + nums[mid] <= upper:
                    low = mid + 1
                else:
                    high = mid - 1

            # Count pairs in the range
            ans += high - left + 1

        return ans
