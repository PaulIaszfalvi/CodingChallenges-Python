class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
              
        result = 0
        reversed_counts = {}

        def reverse_number(n):
            reversed_num = 0
            while n > 0:
                digit = n % 10
                reversed_num = reversed_num * 10 + digit
                n = n // 10
            return reversed_num
      
        # Brute force solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + reverse_number(nums[j]) == reverse_number(nums[i]) + nums[j]:
        #             result += 1

        for num in nums:
            reversed_num = reverse_number(num)
            diff = num - reversed_num
            result += reversed_counts.get(diff, 0)
            result %= 10**9 + 7
            reversed_counts[diff] = reversed_counts.get(diff, 0) + 1
            
        return result
    

        # Online solution

        # MOD = 10 ** 9 + 7
        # num_diff = [i - int(str(i)[::-1]) for i in nums]  # nums[i] - rev(nums[i])

        # res = 0
        # for i in Counter(num_diff).values():
        #     res += i * (i -1) // 2                # nC2 as we need no of pairs 

        # return res % MOD