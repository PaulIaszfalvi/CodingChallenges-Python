class Solution:
    def hammingWeight(self, n: int) -> int:
        #Solution Fastest
        count = 0

        for i in list(str(bin(n))):
            if i == "1":
                count += 1
        return count
    
        #Solution 2
        # n = bin(n)[2:]
        # ans = 0
       
        # for x in n:           
        #     if x == '1':
        #         ans += 1
        # return ans
    
n = 1011
print(Solution().hammingWeight(n))