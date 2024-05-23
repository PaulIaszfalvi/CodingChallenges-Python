class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        # Solution 3 

        nums.sort()
        n = len(nums)
        count = [0]
        
        def dfs(index, chosen):
            if index == n:
                if chosen:
                    count[0] += 1
                return
            
            # Option 1: Skip the current number
            dfs(index + 1, chosen)
            
            # Option 2: Include the current number if it's valid
            can_add = True
            for i in chosen:
                if abs(nums[index] - nums[i]) == k:
                    can_add = False
                    break
            
            if can_add:
                dfs(index + 1, chosen + [index])
        
        dfs(0, [])
        return count[0]
    
    #   # Solution 2

        def dfs(index, path):
            if index == len(nums):
                if path:
                    count[0] += 1
                return
            
            dfs(index + 1, path)
            
            add_num = True
            for num in path:
                if abs(nums[index] - num) == k:
                    add_num = False
                    break
            
            if add_num:
                dfs(index + 1, path + [nums[index]])
        
        count = [0]
        dfs(0, [])
        return count[0]

        # Solution 1
         
        def isBeautiful(s):
            
            d = {}

            for x in s:
                d[x] = d.get(x, 0) + 1
            
            for key, value in d.items():
                if abs(k - key) in d:
                    return False

            return True

        def subs(nums):
            subsets = [[]]  # Initialize with an empty subset
            for num in nums:
                subsets += [subset + [num] for subset in subsets]
            return subsets

        subsets = subs(nums)       
        ans = []

        for x in subsets[1:]: # Ignore empty subset             
            if isBeautiful(x):
                ans.append(x)

        return len(ans)