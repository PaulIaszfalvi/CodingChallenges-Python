class Solution:
    def maxCoins(self, piles: List[int]) -> int:


        # Solution 2
        piles.sort()
        return sum(piles[len(piles)//3::2])
    
        # Solution 1
        
        # ans = 0
        # l = len(piles)-2
        # i = 0

        # piles.sort()

        # while l > 0 and l > i:           
        #     ans += piles[l]
        #     l -= 2
        #     i += 1
        
        # return ans