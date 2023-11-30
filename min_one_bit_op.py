class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)

        # Solution 1 brute force
        # ans = 0
        # num = list(bin(n)[2:])
        # i = 0
        # j = len(num)-1

        # print(num)

        # while i <= j:
        #     if num[i] == '1':
        #         if num[j] == '0':
        #             num[j] = '1'
        #             ans += 1
        #         else:
        #             num[i] = '0'
        #             ans += 1    
        #         i+= 1       
        #     else: 
        #         ans += 2
           
       
        # return ans

n = 9
print(Solution().minimumOneBitOperations(n))