class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:

        possibilities = 0
        count = 0

        for i in flowerbed:
            if i == 0:
                count += 1
                
                if count == 3:
                    count = 1
                    possibilities += 1
            else:
                count = 0
        
        return n <= possibilities
    

flowerbed = [1,0,0,0,1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))