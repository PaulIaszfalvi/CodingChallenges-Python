class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        # Solution 1

        n = len(grid)
        thieves = set((x, y) for x in range(n) for y in range(n) if grid[x][y] == 1)

        def manhattan_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        def getty(x, y, min_dist_to_thief, visited):
            if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited:
                return float('-inf')

            visited.add((x, y))

            if (x, y) in thieves:
                min_dist_to_thief = 0

            if x == n - 1 and y == n - 1:
                return min_dist_to_thief

            min_dist_to_thief += 1
            max_safeness_factor = 0

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                min_dist_to_next_thief = min(min_dist_to_thief, min(manhattan_distance(nx, ny, tx, ty) for tx, ty in thieves))
                max_safeness_factor = max(max_safeness_factor, getty(nx, ny, min_dist_to_next_thief, visited))

            return max_safeness_factor

        return getty(0, 0, float('inf'), set())
    

        # Online solution

class Solution:
    def __init__(self):
        self.roww = [0, 0, -1, 1]
        self.coll = [-1, 1, 0, 0]

    def bfs(self, grid, score, n):
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    score[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            s = score[x][y]

            for i in range(4):
                new_x = x + self.roww[i]
                new_y = y + self.coll[i]

                if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > s + 1:
                    score[new_x][new_y] = s + 1
                    q.append((new_x, new_y))

    def maximumSafenessFactor(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0

        score = [[float('inf')] * n for _ in range(n)]
        self.bfs(grid, score, n)

        vis = [[False] * n for _ in range(n)]
        pq = [(-score[0][0], 0, 0)]
        heapq.heapify(pq)

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            vis[x][y] = True

            for i in range(4):
                new_x = x + self.roww[i]
                new_y = y + self.coll[i]

                if 0 <= new_x < n and 0 <= new_y < n and not vis[new_x][new_y]:
                    s = min(safe, score[new_x][new_y])
                    heapq.heappush(pq, (-s, new_x, new_y))
                    vis[new_x][new_y] = True

        return -1