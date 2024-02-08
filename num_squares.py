class Solution:
    def numSquares(self, n: int) -> int:

        # Online solution DP

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            min_val = float('inf')
            j = 1
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        return dp[n]

        # Solution 5 (DP)

        ps = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        
        # Create a dp list to store the minimum number of perfect squares for each number from 1 to n
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for square in ps:
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]

        # Solution 4 

        ps = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
        ans = []
        ind = next((i for i, v in enumerate(ps) if v < n), None)

        if n in ps:
            return 1

        for a in ps:       
            for b in ps[::-1]:
                if (a + b) == n:
                    ans.append(2)
                for c in ps:
                    if (a + b + c) == n:
                        ans.append(3)        

        if ans:
            return min(ans)
        else:
            return 4

        # Solution 3 (Lagrange's Four Square Theorem)

        ps = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
        c = 0
        # (ignore) ind = next((i for i, v in enumerate(ps) if v < n), None)

        if n in ps:
            return 1

        for a in ps:       
            for b in ps[::-1]:
                if (b + c) == n or (a + b) == n:
                    print(b, c)
                    return 2
                for c in ps:
                    if (a + b + c) == n:
                        print(a, b, c)
                        return 3               

        return 4        

        # Solution 2 (slight optimized)

        ps = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
        c = 0

        if n in ps:
            return n

        while n > 1:
            for x in ps[::-1]:
                if x <= n:
                    n = n-x
                    c += 1
                    break                 

        return c

        # Solution 1 brute force

        # ps = [i ** 2 for i in range(1, int(10000 ** 0.5) + 1)]

        # if n in ps:
        #     return n

        # ans = []

        # while n > 1:
        #     for x in ps[::-1]:
        #         if x <= n:
        #             n = n-x
        #             ans.append(x)
        #             break                 

        # return len(ans)

            