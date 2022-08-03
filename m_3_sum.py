from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
           
        nums.sort()   

        total = 0
        results_list = []
        
        for i, e in enumerate(nums[:len(nums)-2]):           

            twoSumResults = self.twoSum(nums[i+1:], e*-1)

            if twoSumResults:
                for items in twoSumResults:
                    results_list.append([e, items[0], items[1]])

        mySet = set(tuple(x) for x in results_list)
        unique_Answers = [ list(x) for x in mySet ]

        return unique_Answers

    def twoSum(self, nums: List[int], target:int) -> List[int]:
        
        numsMap = {}
        indexOfAnswers = []
        answers = []

        for i, n in enumerate(nums):

            complement = target - n
            
            if complement in numsMap:
                for key, value in numsMap.items():
                    if value == numsMap[complement]:
                        mapKey = key

                indexOfAnswers.append([n, mapKey]) 
                
            numsMap[n] = i
        return indexOfAnswers


sol = Solution()

nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))

nums = [0,0,0]
print(sol.threeSum(nums))

nums = [0,1,1]
print(sol.threeSum(nums))
