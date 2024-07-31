class Solution:
    def passThePillow(self, n: int, time: int) -> int:

      # Solution 2

      direction = 1  # 1 for forward, -1 for backward
        position = 1

        for _ in range(time):
            if position == 1:
                direction = 1
            elif position == n:
                direction = -1
            
            position += direction

        return position

      # Solution 1

        c = 1
        
        while time > 0:
            c += 1
            time -= 1

            if abs(c) == n or abs(c) == 1:
                c *= -1
        
        return abs(c)
