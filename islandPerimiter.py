class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # Online Solution
       
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter


        # Solution 2 (partial)

        s = set()
        rows = len(grid)
        cols = len(grid[0])      
        c = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:                    

                    # Check each adjacent cell
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        c += 1
                    if i + 1 >= rows or grid[i + 1][j] == 0:
                        c += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        c += 1
                    if j + 1 >= cols or grid[i][j + 1] == 0:
                        c += 1

        return c



        # Solution 1 (partial) 

        s = set()
        rows = len(grid)
        cols = len(grid[0])  
        c = 0       

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:                    
                    s.add((i, j)) 
                    c += 4

                     # Check each adjacent cell
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        c -= 1
                    if i + 1 >= rows or grid[i + 1][j] == 0:
                        c -= 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        c -= 1
                    if j + 1 >= cols or grid[i][j + 1] == 0:
                        c -= 1

        print(s)

        return len(s) * 4
