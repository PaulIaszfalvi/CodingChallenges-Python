class Solution:

    def hasPair(self, nums, target):

        my_set = sorted(set(nums))
        solutions = []

        for i in range(len(nums)-2):
            pair = target - nums[i]
            if pair in my_set:
                solutions.append([nums[i], pair])

        return solutions

nums = [0, -1, 2, -3, 1]
target = -2

sol = Solution()
print(sol.hasPair(nums, target))
print(sol.hasPair(nums, -4))
print(sol.hasPair(nums, 3))

A = [1, 4, 45, 6, 10, -8]
n = 16
print(sol.hasPair(A, n))