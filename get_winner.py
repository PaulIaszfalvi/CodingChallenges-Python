class Solution:
    def getWinner(self, a: List[int], k: int) -> int:

        # Solution 1 prototype
        
        # w1, w2 = 0, 0
        # biggest = max(a)

        # while k > 0:
        #     print(a)
        #     first = a[0]
        #     second = a[1]
                
        #     if first > second:
        #         a.remove(second)
        #         a.append(second)
        #         w1 += 1
        #         w2 = 0              
        #     else:
        #         a.remove(first)
        #         a.append(first)
        #         w2 += 1
        #         w1 = 0    

        #     if w1 >= k or w2 >= k or first == biggest:                    
        #         break

        # return a[0]

        # Solution 2

        if k == 1:
            return max(a[0], a[1])
        if k >= len(a):
            return max(a)

        winner = a[0]
        wins = 0

        for i in range(1, len(a)):
            
            if winner > a[i]:
                wins += 1
            else:
                winner = a[i]
                wins = 1

            if wins >= k:
                break
        
        return winner
