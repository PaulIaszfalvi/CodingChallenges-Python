from typing import List

# class TwoSum:
#       def twoSum(self, nums: List[int], target: int) -> List[int]:

#         numsMap = {}
#         indexOfAnswers = []

#         for i, n in enumerate(nums):

#             complement = target - n
            
#             if complement in numsMap:
#                 indexOfAnswers.append(i)                      
#                 indexOfAnswers.append(numsMap[complement])          
                
#             numsMap[n] = i
        
#         return indexOfAnswers

    # def __init__(self) -> None:
    #     self.nums = nums
    #     self.target = target

    # def findIndex(self, nums: List[int], target:int) -> List[int]:
        
    #     left = 0
    #     right = len(nums)-1
    #     total = 0

    #     while(True):            
    #         total = nums[left] + nums[right]

    #         if total == target:
    #             return [left, right]
    #         elif total > target: 
    #             right -= 1
    #         else:
    #             left += 1

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complementMap = dict()

        for i in range(len(nums)):
            complement = target - nums[i]

            if nums[i] in complementMap:
                print(complementMap)
                return [complementMap[nums[i]], i]
            else:
                complementMap[complement] = i

       


nums = [2,7,11,15]
target = 9

twoSum = TwoSum()
print(twoSum.twoSum(nums, target))

nums =[-1,0,1,2,-1,-4]
target = 0
print(twoSum.twoSum(nums, target))