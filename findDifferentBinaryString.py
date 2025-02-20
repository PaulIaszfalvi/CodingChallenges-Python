class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])  
        
        num_set = {int(b, 2) for b in nums}  

        for i in range(2 ** n):  
            if i not in num_set:
                return format(i, f'0{n}b') 
