class Solution:
    def numberOfWays(self, corridor: str) -> int:

        # Solution 2
        # x = 1 # 0 seat
        # y = 0 # 1 seat
        # z = 0 # 2 seats
        # for char in corridor:
        #     if char == 'S':
        #         x, y, z = 0, x + z, y
        #     else:
        #         x, y, z = x + z, y, z
        # return z % (10**9+7) 
    
        # Solution 1
        # seat, res, plant = 0, 1, 0
        # for i in corridor:
        #     if i=='S':
        #         seat += 1
        #     else:
        #         if seat == 2:
        #             plant += 1
        #     if seat == 3:
        #         res = res*(plant+1) % (10**9 + 7)
        #         seat , plant = 1 , 0
        # if seat != 2:
        #     return 0
        # return res
