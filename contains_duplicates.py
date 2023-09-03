class Solution:
    def containsDuplicate(self, nums) -> bool:

        return len(nums) != len(set(nums))
        
        # map = {}
        # result = False        
        
        # for e in nums: 
        #     map[e] = map.get(e, 0) + 1
        
        # for key,value in map.items():
        #     if value > 1:
        #         result = True
            
        # return result

nums = [1, 2, 3, 4, 1]
sol = Solution()
print(sol.containsDuplicate(nums))