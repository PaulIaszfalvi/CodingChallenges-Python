from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #negative nubers, zeroes and positives
        n, z, p = [], [], []
        results = set()      

        for e in nums:
            if e < 0:
                n.append(e)
            elif e == 0:
                z.append(e)
            else:
                p.append(e)

        N, P = set(n), set(p)

        #Base case, if we have 3 zeroes, then that's an answer
        if len(z) > 2:
            results.add((0,0,0))

        #If there are zeroes
        if z: 
            for e in N:
                if e*-1 in P:
                    results.add((e * -1, 0, e))
                        
        #Find multiple negatives and one positive
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    results.add(tuple(sorted([n[i],n[j],target])))

        #Find multiple positives and one negative
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = (p[i] + p[j]) * -1
                if target in N:
                    results.add(tuple(sorted([p[i], p[j], target])))

        return results


        #First Solution
    #        
    #     nums.sort()   

    #     total = 0
    #     results_list = []
        
    #     n, p, z = [], [], []
        
    #     for e in nums:
    #         if e < 0:
    #             n.append(e)
    #         elif e == 0:
    #             z.append(e)
    #         else:
    #             p.append(e)
                
    #     if len(z) > 2:
    #         results_list.append([0,0,0])
            
    #     if z:
    #         nums = p + [0] + n
    #     else: 
    #         nums = p + n
        
    #     for i, e in enumerate(nums[:len(nums)-2]):           

    #         twoSumResults = self.twoSum(nums[i+1:], e*-1)

    #         if twoSumResults:
    #             for items in twoSumResults:
    #                 results_list.append([e, items[0], items[1]])

    #     mySet = set(tuple(x) for x in results_list)
    #     unique_Answers = [ list(x) for x in mySet ]

    #     return unique_Answers

    # def twoSum(self, nums: List[int], target:int) -> List[int]:
        
    #     numsMap = {}
    #     indexOfAnswers = []
    #     answers = []

    #     for i, n in enumerate(nums):

    #         complement = target - n
            
    #         if complement in numsMap:
    #             for key, value in numsMap.items():
    #                 if value == numsMap[complement]:
    #                     mapKey = key

    #             indexOfAnswers.append([n, mapKey]) 
                
    #         numsMap[n] = i
    #     return indexOfAnswers
        


sol = Solution()

nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

nums = [0,0,0]
print(sol.threeSum(nums))

nums = [0,1,1]
print(sol.threeSum(nums))

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(sol.threeSum(nums))
