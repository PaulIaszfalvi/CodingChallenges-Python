class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        # Solution 2 
        m, n = len(grid), len(grid[0])
        
        diff = [[0] * n for _ in range(m)]
        
        onesRow = [sum(row) for row in grid]
        zerosRow = [n - ones for ones in onesRow]
       
        onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        zerosCol = [m - ones for ones in onesCol]
               
        for i in range(m):
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        return diff
       
        # Solution 1 prototype 

        # def get_column_sum(col_idx):
        #     return sum(row[col_idx] for row in grid)
    
        # zeroes_x = len(grid[0])
        # zeroes_y = len(grid)
        # y = 0

        # for row in grid:            
        #     for x in range(len(row)): 
        #         ones_x = sum(row)
        #         ones_y = get_column_sum(x)
        #         grid[y][x] = ones_x + ones_y - (zeroes_x - ones_x) - (zeroes_y - ones_y)
        #     y += 1

        # return grid

        # Cool online solution

        m, n = len(grid), len(grid[0])

        rowSum, colSum = list(map(sum, grid)), list(map(sum, chain(zip(*grid))))
        
        return [[2*(rowSum[r] + colSum[c]) - m-n
                 for c in range(n)] for r in range(m)]
