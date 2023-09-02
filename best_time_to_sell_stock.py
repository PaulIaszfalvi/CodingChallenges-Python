class Solution(object):

    def maxProfit(self, prices):

        max_profit = 0
        min_price = prices[0]

        for price in prices: 
            min_price = price if price < min_price else min_price
            profit = price - min_price
            max_profit = profit if profit > max_profit else max_profit

        return max_profit


        
L1 = [1, 4, 3]
L2 = [2,1,2,0,1]
L3 = [7,6,5,4,3,2,1]
sol = Solution()
print(sol.maxProfit(L1))
print(sol.maxProfit(L2))
print(sol.maxProfit(L3))