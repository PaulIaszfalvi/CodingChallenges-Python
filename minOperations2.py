class Solution:
    def minOperations(self, nums: List[int]) -> int:

      # Solution 2

        n = len(nums)
        flip_count = 0  # Tracks how many times we’ve flipped up to this point
        operations = 0  # Total flips performed
        queue = deque()  # Stores indices where flips end

        for i in range(n):
            # Remove flips that are no longer affecting the current index
            if queue and queue[0] == i:
                queue.popleft()
                flip_count ^= 1  # Flip toggling back

            # If current bit is still `0` after flips, we need a new flip
            if nums[i] ^ flip_count == 0:
                if i + 2 >= n:  # Not enough room to flip 3 elements
                    return -1
                
                operations += 1
                flip_count ^= 1  # New flip affects subsequent elements
                queue.append(i + 3)  # Flip stops affecting after i+3

        return operations

      # Solution 1
      
        def flip(start):
            for i in range(start, min(start + 3, len(nums))):
                nums[i] = 1 - nums[i]  # Flip between 0 and 1

        count = 0
        for i in range(len(nums) - 2):  # Ensure we don't go out of bounds
            if nums[i] == 0:
                flip(i)
                count += 1
        
        return count if all(x == 1 for x in nums) else -1
