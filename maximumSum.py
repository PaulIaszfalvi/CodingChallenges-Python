class Solution:
    def maximumSum(self, nums: List[int]) -> int:

      # Trial Solution 1

        ans = 0
        
        for i in range(len(nums)):

            sum_i = nums[i] % 10 + math.floor(nums[i] / 10)

            for j in range(i, len(nums)):

                sum_j = nums[j] % 10 + math.floor(nums[j] / 10)

                if sum_i == sum_j and i != j:
                    ans = max(ans, nums[i] + nums[j])

        return -1 if ans == 0 else ans

# Solution 1 with TLE

class Solution:

    def get_sum(self, num: int) -> int:
     
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        ans = 0
        digit_sums = {}

        for i in range(len(nums)):
            sum_i = self.get_sum(nums[i])

            for j in range(i + 1, len(nums)):  # Avoid i == j
                sum_j = self.get_sum(nums[j])

                if sum_i == sum_j:
                    ans = max(ans, nums[i] + nums[j])

        return -1 if ans == 0 else ans

# Solution 2

class Solution:
    def get_sum(self, num: int) -> int:
        return sum(int(digit) for digit in str(num))  

    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        digit_sums = {}

        for num in nums:
            sum_digits = self.get_sum(num)

            if sum_digits in digit_sums:
                ans = max(ans, num + digit_sums[sum_digits])

            digit_sums[sum_digits] = max(digit_sums.get(sum_digits, 0), num)

        return ans

