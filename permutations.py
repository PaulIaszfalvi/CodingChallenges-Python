class Solution:
    def permute(self, nums):
        
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)


nums = [1, 2, 3, 4]
print(Solution().permute(nums))

#write a permutation 
class permutation:
    def permute(self,nums):
        res = []
        self.backtracking(nums,[],res)
        return res
    def backtracking(self,nums,subset,res):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in subset:
                self.backtracking(nums,subset+[i],res)