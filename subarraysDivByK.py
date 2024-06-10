class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

      # Solution 2

        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum < 0:
                prefix_sum += k 
            count += remainder_count.get(prefix_sum, 0)
            remainder_count[prefix_sum] = remainder_count.get(prefix_sum, 0) + 1

        return count

      # Solution 1
        
        def subs(arr):
            n = len(arr)
            result = []
            for i in range(n):
                for j in range(i, n):
                    result.append(sum(arr[i:j+1]))
            return result

        count = 0
        s = subs(nums)

        for x in s:
            if x % k == 0:
                count += 1

        return count
