class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Solution 2 O(n) O(1) (Incomplete)

        p1, p2 = 1, 2
        l = len(nums)

        # Get a positive
        if nums[0] < 0:
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[0], nums[i] = nums[i], nums[0]
                    break
        
        while p1 <= l and p2 <= l:

            if nums[p1-1] < 0 and nums[p1] < 0:
                p2 += 1

            if nums[p1-1] > 0 and nums[p1] < 0:
                p1 += 1

            if nums[p1-1] > 0 and nums[p1] > 0 and nums[p2] < 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1

            p2 += 1            
        
        return nums
        

        # Solution 1 (Brute force) O(n)

        p, n, ans = [], [], []

        for x in nums:
            if x > 0:
                p.append(x)
            else:
                n.append(x)

        for i in range(len(p)):
            ans.append(p[i])
            ans.append(n[i])

        return ans