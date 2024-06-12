class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Dutch National Flag Alogrithm

        n = len(nums)
        left, mid, right = 0, 0, n - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


        # Solution 3

        n = len(nums)
      
        z, o, t = 0, 0, 0

        for x in nums:
            match x:
                case 0:
                    z += 1
                case 1:
                    o += 1
                case 2:
                    t += 1

        for i in range(n):
            if z > 0:
                nums[i] = 0
                z -= 1
            elif o > 0:
                nums[i] = 1
                o -= 1
            else:
                nums[i] = 2

        # Solution 2

        n = len(nums)
      
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:                 
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        # Solution 1
        
        a, b = 0, 1

        while a < len(nums):
            while b < len(nums):
                if nums[a] > nums[b]:
                    nums[a], nums[b] = nums[b], nums[a]
                b += 1
            
            a += 1
            b = a + 1
