class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # one = sum(x for x in nums[::2])
        # two = sum(x for x in nums[1::2])

        # return max(one, two)

        r1,r2 = 0,0
        for i in nums:
            temp = max(i+r1,r2)
            r1 = r2
            r2 = temp
        return r2