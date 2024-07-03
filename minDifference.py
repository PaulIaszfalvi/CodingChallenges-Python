class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return 0

        nums.sort()
        print(nums)

        a1 = abs(nums[-4] - nums[0])
        a2 = abs(nums[-3] - nums[1])
        a3 = abs(nums[-2] - nums[2])
        a4 = abs(nums[-1] - nums[3])

        return min(a1, a2, a3, a4)

        # nums.sort()
        # print(nums)
        # temp = nums[len(nums) // 2]
        # nums[0] = temp
        # nums[-1] = temp
        
        # if abs(temp - nums[1]) < abs(temp - nums[-2]):
        #     nums[-2] = temp
        # else:
        #     nums[1] = temp
        # print(nums)
        # mi = min(nums)
        # ma = max(nums)

        # return ma - mi

        
