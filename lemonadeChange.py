class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # d = {}

        # for x in bills:
        #     d[x] = d.get(x, 0) + 1

        f, t = 0, 0

        for x in bills:
 
            if x == 5:
                f += 1
            elif x == 10:
                if f == 0:
                    return False
                f -= 1
                t += 1
            else:
                if t > 0 and f > 0:
                    t -= 1
                    f -= 1
                elif t == 0 and f > 2:
                    f -= 3
                else:
                    return False

        return True
