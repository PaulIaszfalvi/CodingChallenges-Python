class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        ans = []
        c = 0

        while c < len(nums) - 2:
            if nums[c + 2] - nums[c] <= k:
                ans.append(nums[c:c+3])
            c += 3
             
        return ans if len(ans) == len(nums) // 3 else []