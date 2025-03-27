class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

      # Solution 2

      d = Counter(nums)  # Count occurrences
        max_key = max(d, key=d.get)  # Get dominant element
        val = d[max_key]  # Total occurrences of dominant element

        f1, f2 = 0, val  # Frequency counters
        
        for x in range(len(nums)):
            if nums[x] == max_key:
                f1 += 1
                f2 -= 1

            l1 = x + 1  # Left segment length
            l2 = len(nums) - l1  # Right segment length

            # Check if both parts satisfy dominance condition
            if f1 * 2 > l1 and f2 * 2 > l2:
                return x
        
        return -1


      # Solution 1 (TLE)
        
        d = Counter(nums)

        max_key = max(d, key=d.get)
        val = d[max_key]

        f1, f2 = 0, val

        for x in range(len(nums)):
            if nums[x] == max_key:
                f1 += 1
                f2 -= 1

                l1 = len(nums[:x+1])
                l2 = len(nums[x+1:])

                if f1 * 2 > l1 and f2 * 2 > l2:
                    return x
        
        return -1
