class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        # Online DP Solution
        
        dp = [0] * 27  # Initialize dynamic programming array to store longest ideal string ending at each character position
        n = len(s)

        for i in range(n - 1, -1, -1):
            cc = s[i]
            idx = ord(cc) - ord('a')
            maxi = float('-inf')

            left = max((idx - k), 0)
            right = min((idx + k), 26)

            for j in range(left, right + 1):
                maxi = max(maxi, dp[j])

            dp[idx] = maxi + 1  # Update dp array with the length of the longest ideal string ending at current position

        return max(dp)  # Return the maximum value in the dp array, which represents the length of the longest ideal string


        # Solution 1 (Brute force)

        # Generate all in order combinations and check the length of each using the algorithm given

        def getLen(string, k):
        
            ans = ''
            slow, fast = 0, 1

            while fast < len(s):               

                diff = abs(ord(s[fast]) - ord(s[slow]))
                              
                if diff <= k:
                    ans += s[slow]
                    slow = fast

                    if fast == len(s) - 1:
                        ans += s[fast]
                
                fast += 1     
          
            return len(ans)

        def permute(s):
            if len(s) == 0:
                return ['']

            result = []
            for combo in permute(s[1:]):               
                result.append(s[0] + combo)              
                result.append(combo)
            return result

        p = permute(s)
        maximum = 0

        for x in p:         
            maximum = max(maximum, getLen(x, k))           

        return maximum


        # Rough Draft
        
        ans = ''

        for i in range(1, len(s)):

            diff = abs(ord(s[i]) - ord(s[i - 1]))

            if diff <= k:
                ans += s[i-1]
                print(s[i-1], s[i], diff)

        if abs(ord(s[len(s)-1]) - ord(s[len(s)-2])) <= k:
            ans += s[-1]

        print(ans)

        return len(ans)