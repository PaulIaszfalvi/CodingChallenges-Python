from typing import List

class TwoSum:

    def __init__(self) -> None:
        self.nums = nums
        self.target = target

    def findIndex(self, nums: List[int], target:int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        total = 0

        while(True):            
            total = nums[left] + nums[right]

            if total == target:
                return [left, right]
            elif total > target: 
                right -= 1
            else:
                left += 1

nums = [2,7,11,15]
target = 9

twoSum = TwoSum()
print(twoSum.findIndex(nums, target))