class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        # Fastest 

        @lru_cache(None)
        def dp(idx,d,curr):
		
            if idx == len(jobDifficulty) and d == 0: return curr
            if idx >= len(jobDifficulty) or  d <= 0: return inf
            
            return min(dp(idx+1,d,max(curr,jobDifficulty[idx])),
                       max(curr,jobDifficulty[idx])+dp(idx+1,d-1,0))
       
        ans = dp(0,d,0)

        return ans if ans != inf else -1

        # A better way based on the answer below 

        n = len(jobDifficulty)

        # Check if it's possible to divide the jobs into 'd' days
        if n < d:
            return -1

        # Initialize the DP array
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for day in range(1, d + 1):
                max_difficulty = 0
                for j in range(i, 0, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[j - 1])
                    dp[i][day] = min(dp[i][day], dp[j - 1][day - 1] + max_difficulty)

        return dp[n][d] if dp[n][d] != float('inf') else -1

        # ChatGPT 

        n = len(jobDifficulty)
        
        # Check if it's possible to divide the jobs into 'd' days
        if n < d:
            return -1

        # Initialize a 2D DP array with all entries set to infinity
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0

        # Iterate over the days
        for day in range(1, d + 1):
            # Iterate over the jobs
            for i in range(1, n + 1):
                max_difficulty = 0
                # Traverse backward to find the maximum difficulty
                for j in range(i, 0, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[j - 1])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + max_difficulty)

        return dp[d][n] if dp[d][n] != float('inf') else -1

        # Solution 1
        
        if len(jobDifficulty) < d:
            return -1

        if len(jobDifficulty) == d:
            return sum(x for x in jobDifficulty)

        jobDifficulty.sort()
        result = 0 

        result += sum(x for x in range(d))
        result += jobDifficulty[-1]

        return result 
