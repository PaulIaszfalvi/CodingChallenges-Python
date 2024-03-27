class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # Solution 2

        if k <= 1:
            return 0  # Since the product will always be greater than or equal to 1
        
        count = 0  # Initialize the count of valid subarrays
        prod = 1   # Initialize the product of elements in the window
        left = 0   # Initialize the left pointer of the window
        
        for right, num in enumerate(nums):
            prod *= num  # Include the current element in the product
            
            # Shrink the window from the left as long as product is greater than or equal to k
            while prod >= k:
                prod /= nums[left]  # Remove the leftmost element from the product
                left += 1  # Move left pointer to the right
            
            # Count the subarrays ending at the current index
            count += right - left + 1
        
        return count


        # Solution 1

        if len(nums) == 1:
            return 1 if nums[0] < k else 0

        c = 0  # Initialize count of valid subarrays
        prod = 1  # Initialize product of elements in the window
        left = 0  # Initialize left pointer of the window

        # Loop through the list using right pointer
        for right, num in enumerate(nums):
            prod *= num  # Include the current element in the product
            # Shrink the window from the left as long as product is greater than or equal to k
            while prod >= k and left <= right:
                prod /= nums[left]  # Remove the leftmost element from the product
                left += 1  # Move left pointer to the right
            c += right - left + 1  # Add the count of valid subarrays ending at the current index

        return c
