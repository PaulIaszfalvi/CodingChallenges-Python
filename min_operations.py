class Solution:
    def minOperations(self, s: str) -> int:

        # Solution 1

        sol1 = sol2 = ''
        count1 = count2 = 0
      
        for i in range(len(s)):

            if i % 2 == 0:
                sol1 += '1'
                sol2 += '0'
            else:
                sol1 += '0'
                sol2 += '1'

        for i in range(len(s)):
            if s[i] != sol1[i]:
                count1 += 1
            if s[i] != sol2[i]:
                count2 += 1

        return min(count1, count2)

        # # Solution 2 prototype

        # first = second = 0

        # for i in range(1, len(s), 2):
        #     if s[i] == s[i-1]:
        #         first += 1

        # for i in range(len(s), 2):
        #     if s[i] == s[i+1]:
        #         second += 1

        # print(first, second)
        # if first != 0 and second != 0:
        #     return min(first, second)
        # else:
        #     return first if first != 0 else second


        # # Solution 1 prototype
        
        # odds = 0
        # evens = 1 if s[0] == s[1] else 0
        
        # for i in range(1, len(s)):
        #     if s[i] == s[i-1]:
        #         if i % 2 == 0:
        #             evens += 1
        #         else:
        #             odds += 1

        # print(odds, evens)
        
        # if odds == 0:
        #     return evens
        # elif evens == 0:
        #     return odds
        # else:
        #     return min(odds, evens)
    
        # Faster online solution
    

        # n=len(s)
        # op0=0
        # for i, c in enumerate(s):
        #     if (i&1)==(ord(c)&1):
        #         op0+=1
        # return min(op0, n-op0)
    
        # Shorter version 
        # n = len(s)
        # count = sum((i & 1) ^ int(c) for i, c in enumerate(s))
        # return min(count, n - count)
    
        # More complex but cool 
    
        # count = reduce(lambda acc, iv: acc + (iv[0] % 2 ^ (iv[1] == '0')), enumerate(s), 0)
        # return min(count, len(s) - count)