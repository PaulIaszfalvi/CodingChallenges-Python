class Solution:
    def numberOfSubstrings(self, s: str) -> int:

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
