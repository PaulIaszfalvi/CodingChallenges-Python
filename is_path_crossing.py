class Solution:
    def isPathCrossing(self, path: str) -> bool:

        # Solution 1 
        
        x = y = 0
        coords = {(x, y)}

        for p in path: 
            switch = {
                'N': (x, y + 1),
                'S': (x, y - 1),
                'E': (x + 1, y),
                'W': (x - 1, y)
            }
            x, y = switch.get(p, (x, y))
            if (x, y) in coords:
                return True
            coords.add((x, y))

        return False