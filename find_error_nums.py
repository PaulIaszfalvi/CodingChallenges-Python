class Solution:
    def findErrorNums(self, nums):
       
       # sum of all numbers
       l = len(nums) * (len(nums)+ 1) // 2
       # sum of unique numbers 
       s = sum(set(nums))
   
       # return duplicate and misisng number 
       return [sum(nums)-s,l-s]