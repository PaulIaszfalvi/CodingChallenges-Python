def longestMonotonicSubarray(self, nums: List[int]) -> int:

        # Solution 2
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        ans = 1
        l_inc = 1
        l_dec = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                l_inc += 1
                l_dec = 1
            elif nums[i - 1] > nums[i]:
                l_dec += 1
                l_inc = 1
            else:
                l_inc = 1
                l_dec = 1

            ans = max(ans, l_inc, l_dec)

        return ans

        # Solution 1

        l = 1
        ans = 0

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                l += 1
            else:
                ans = max(ans, l)
                l = 1 

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                l += 1
            else:
                ans = max(ans, l)
                l = 1 

        return ans
