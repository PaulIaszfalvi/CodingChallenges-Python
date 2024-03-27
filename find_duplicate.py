class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Solution 3

        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find the intersection point of the two pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        # Solution 2

        s = set()

        for x in nums:
            if x in s:
                return x
                
            s.add(x)
            
        

        # Solution 1
        
        d = {}

        for x in nums:
            d[x] = d.get(x, 0) + 1

            if d[x] > 1:
                return x
        