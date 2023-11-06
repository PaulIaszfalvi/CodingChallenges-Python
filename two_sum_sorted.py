class Solution:
    def twoSum(self, numbers, target: int):
        
        i = 0
        j = len(numbers) -1
        
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1 , j + 1]
            
            if s > target:
                j-=1
            else:
               i+=1 
        
        return []

num = [1,2,3,4,5,6,7,8,9,10]
target = 8
print(Solution().twoSum(num, target))