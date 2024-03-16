class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # Solution 2

        count = 0
        max_length = 0
        hash_map = {0: -1}  # Initialize hashmap with count 0 at index -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in hash_map:
                max_length = max(max_length, i - hash_map[count])
            else:
                hash_map[count] = i
        
        return max_length
        

        # Solution 1
        o, z = 0, 0

        for x in nums:
            if x == 1:
                o += 1
            else:
                z += 1

        return min(o, z) * 2