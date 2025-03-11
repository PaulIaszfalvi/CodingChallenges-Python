class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # Optimized solutions
          # 1
        abc = [-1, -1, -1]
        count, right = 0, 0
        while right < len(s):
            abc[ord(s[right]) - ord('a')] = right
            minIndex = min(abc)
            count += (minIndex + 1)
            right += 1
        return count

            # 2
        
        count = { 'a': 0, 'b': 0, 'c': 0 }
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1  # Expand the window

            while all(count[ch] > 0 for ch in "abc"):  # If 'a', 'b', and 'c' are all present
                res += len(s) - r  # All substrings from l to the end are valid
                count[s[l]] -= 1  # Shrink the window
                l += 1

        return res

        # Solution 2

        substrings = []
        n = len(s)
        count = 0

        for i in range(n):
            for j in range(i, n):
                if len(set(s[i:j+1])) == 3:
                    count += 1

        return count

        # Solution 1
        substrings = []
        n = len(s)
        count = 0

        for i in range(n):
            for j in range(i, n):
                substrings.append(s[i:j+1])

        for s in substrings:
            if len(set(s)) == 3:
                count += 1

        return count
