class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Solution 3 

        i=2
        while i<len(nums):
            if nums[i-2]==nums[i-1]==nums[i]:
                nums.pop(i)
                i-=1
            i+=1
        return len(nums)        
    
        # Solution 2

        c = 1  # Initialize counter to 1 for the first occurrence of the first element
        j = 1  # Initialize index j to 1 (first element already in place)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                c += 1
            else:
                c = 1  # Reset counter for new element
            if c <= 2:
                nums[j] = nums[i]  # Keep only the first two occurrences
                j += 1

        return j


        # Solution 1

        c = 0
        cur = nums[0]
        
        for i in range(len(nums)):
            if nums[i] == cur:
                c += 1
            if c > 2:
                nums[i] = '_'                
            if nums[i+1] != cur:
                cur = nums[i]
                c = 1
        print(nums)
        l, r = 0, 0

        while l < len(nums) - 1 or r < len(nums) - 1:
           
            while l < len(nums)-1 and nums[l] != '_':
                l += 1             
            r = l + 1
            while r < len(nums)-1 and nums[r] == '_':
                r += 1
            
            nums[l], nums[r] = nums[r], nums[l]
           
            l += 1
        print(nums)

        return l
