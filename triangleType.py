class Solution:
    def triangleType(self, nums: List[int]) -> str:
        d = set(nums)

        s1 = nums[0] + nums[1]
        s2 = nums[1] + nums[2]
        s3 = nums[0] + nums[2]

        if s1 <= nums[2] or s2 <= nums[0] or s3 <= nums[1]:
            return "none"

        if len(d) == 1:
            return "equilateral"
        if len(d) == 2:
            return "isosceles"
        else:
            return "scalene"
