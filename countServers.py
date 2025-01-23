class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        # Solution 2
        
        rows = len(grid)
        cols = len(grid[0])

        # Step 1: Count the number of 1's in each row and column
        row_count = [0] * rows
        col_count = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Step 2: Count servers that can communicate
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    ans += 1

        return ans

        # Solution 1

        ans = 0 
        rows = len(grid)
        cols = len(grid[0])
        check = False

        for i in grid:
            for j in i:
                if j == 1:
                    ans += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Check up
                    if i > 0 and grid[i - 1][j] == 1:
                        check = True

                    # Check down
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        check = True

                    # Check left
                    if j > 0 and grid[i][j - 1] == 1:
                        check = True

                    # Check right
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        check = True

            if check:
                continue
            else:
                ans -= 1
            check = False

        return ans
