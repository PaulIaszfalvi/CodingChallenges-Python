class Solution:
    def getSumAbsoluteDifferences(self, nums):
        
        # Online Solution

        n=len(nums)
        A=0
        B=sum(nums)
        ans=[0]*n

        for i, x in enumerate(nums):
            ans[i]=(2*i-n)*x+B-A
            A+=x
            B-=x
        return ans


        # Solution 1
        # results = []

        # for i in range(len(nums)):
        #     result = 0
        #     for j in range(len(nums)):
        #         result += abs(nums[i] - nums[j])
        #     results.append(result)
        # return results