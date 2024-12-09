class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        # Solution 2

        results = []

        for q in queries:
            is_special = True
            for i in range(q[0], q[1] - 1): 
                if nums[i] % 2 == nums[i + 1] % 2:
                    is_special = False
                    break
            results.append(is_special)
        
        return results


        # Solution 1

        results = []
        ans = True
        
        for q in queries:
            for i in range(q[0], q[1]):
                if nums[i] % 2 == nums[i+1] % 2:
                    ans = False
                    break
            if ans:
                results.append(ans)
            else:
                results.append(ans)
                ans = True
        
        return results
            

             
