class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        # Alternate solution with for loop

        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i] + k >= nums[i+2]:
                ans.append(nums[i:i+3])
            else:
                return []
        return ans

        #Solution 1
        
        nums.sort()
        ans = []
        c = 0

        while c < len(nums) - 2:
            if nums[c + 2] - nums[c] <= k:
                ans.append(nums[c:c+3])
            c += 3
             
        return ans if len(ans) == len(nums) // 3 else []