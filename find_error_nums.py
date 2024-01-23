class Solution:
    def findErrorNums(self, nums):
       
       l = len(nums) * (len(nums)+ 1) // 2

       s = sum(set(nums))
   
       return [sum(nums)-s,l-s]