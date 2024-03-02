class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Solution 3

        for i, v in enumerate(nums):
                nums[i] = v * v
        
        nums.sort()

        return nums

        # Solution 2

        ans = [x * x for x in nums]
        ans.sort()

        return ans
       
        # Solution 1

        ans = []

        for x in nums:
            ans.append(x ** 2)

        return sorted(ans)