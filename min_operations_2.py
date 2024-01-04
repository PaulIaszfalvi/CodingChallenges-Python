class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # Solution 4

        d = {}
        o = 0

        for x in nums:
            d[x] = d.get(x, 0) + 1

        for t in d.values():
            if t == 1:
                return -1
            o += t // 3
            if t % 3:
                o += 1

        return o
    
        # Solution 3
    
        # d = {}
        # o = 0

        # for x in nums:
        #     d[x] = d.get(x, 0) + 1

        # for x in d:
        #     if d[x] == 1:
        #         return -1

        #     if d[x] % 3 == 0:
        #         o += d[x] // 3
               
        #     else:
        #         o += d[x] // 3 + 1               
            
        # return o 

        # Solution 2 prototype 

        # d = {}
        # o = 0

        # for x in nums:
        #     d[x] = d.get(x, 0) + 1

        # for x in list(d.keys()):
        #     if x == 1:
        #         break
            
        #     result = d[x] % 3

        #     if result == 0:
        #         o += d[x] // 3
        #         del d[x]          
        #     elif result == 1:
        #         o += d[x] // 3 + 1
        #         del d[x]
        #     else:
        #         o += d[x] // 2
        #         del d[x]

        # return o if len(d) == 0 else -1
        

        # Solution 1

        # d = {}
        # o = 0

        # for x in nums:
        #     d[x] = d.get(x, 0) + 1

        # for x in list(d.keys()):
        #     print(x, d[x])
        #     if d[x] % 3 == 0:
        #         o += d[x] // 3
        #         del d[x]
        #     elif d[x] % 2 == 0:
        #         while d[x] > 4:
        #             d[x] - 3
        #             o += 1
        #         o += d[x] // 2
        #         del d[x]

        # return o if len(d) == 0 else -1

        # Online alternative

        # mp = Counter(nums)
        
        # count = 0
        # for t in mp.values():
        #     if t == 1:
        #         return -1
        #     count += t // 3
        #     if t % 3:
        #         count += 1
                
        # return count