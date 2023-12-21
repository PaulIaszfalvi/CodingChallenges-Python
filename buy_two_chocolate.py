class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        # Solution 2

        s1, s2 = 100, 100

        for x in prices:
            if x < s1:
               s2 = s1
               s1 = x
            elif x < s2:
                s2 = x

        result = money - s1 - s2

        return result if result >= 0 else money

        # Solution 1
        
        # prices.sort()
        # result = money - sum(prices[:2])
        # return result if result >= 0 else money
    
        # Faster online O(n)

        # heapify(prices)
        # sm = heappop(prices)+heappop(prices)
        # return money - sm if sm <= money else money