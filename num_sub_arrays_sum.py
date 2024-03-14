class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:


        # Solution 2

        count = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - goal in count:
                total_subarrays += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1

        return total_subarrays
    
        # Solution 1

        count = 0
        prefix_sum = 0
        sum_count = {0: 1}  # Stores the count of prefix sums encountered

        for num in nums:
            prefix_sum += num
            # Check if there exists a prefix sum such that prefix_sum - goal = previous_prefix_sum
            previous_prefix_sum = prefix_sum - goal
            if previous_prefix_sum in sum_count:
                count += sum_count[previous_prefix_sum]

            # Increment the count of the current prefix sum
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

        return count