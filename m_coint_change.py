class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:  
        
        count = 0
        
        for e in coins[::-1]:
            
            if amount // e is not 0:
                count += amount // e
                amount = amount % e
                        
        return -1 if amount is not 0 else count