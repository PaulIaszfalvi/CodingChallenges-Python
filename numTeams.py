class Solution:
    def numTeams(self, rating: List[int]) -> int:

        # Fast online Sol



        l = []

        sr = sorted(rating)

        low = {}

        for idx,r in enumerate(sr):

            low[r] = idx

        res = 0

        n = len(rating)

        for idx,r in enumerate(rating):

            i = bisect.bisect(l, r)

            l.insert(i,r)

            j = low[r] - i

            res+=i*(n-1-idx-j)+j*(idx-i)

        return res

    def numTeams2(self, rating: List[int]) -> int:

        ans,n = 0,len(rating)

        for j in range(n):

            # for any middle position j find counts less than rating[j] in  [0..j) and (j..n) ranges

            llt,lgt = 0,0

            for i in range(j):

                llt += rating[i] < rating[j]

                lgt += rating[i] > rating[j]

            rlt,rgt = 0,0

            for k in range(j+1,n):

                rlt += rating[k] < rating[j]

                rgt += rating[k] > rating[j]

            ans += llt*rgt + lgt*rlt 

        return ans

    # bf,tle

    def numTeams1(self, rating: List[int]) -> int:

        ans,n = 0,len(rating)

        for i in range(n):

            for j in range(i+1,n):

                for k in range(j+1,n):

                    ans += 1 if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k] else 0

        return ans      

        # Solution 2 (TLE)

        n = len(rating)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if the team is valid (either increasing or decreasing)
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        count += 1

        return count

        # Solution 1 (invalid because it checks all permutations)

        perms = list(permutations(range(len(rating)), 3))
        count = 0

        for i, j, k in perms:
            if i < j < k:
                if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                    count += 1
    
        return count
