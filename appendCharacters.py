class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        # Solution 2

         i, j = 0, 0 

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j

        # Solution 1
        if t in s:
            return 0

        count = 0

        for _ in range(len(t)):
            t = t[:-1]
            count += 1

            if t in s:
                return count

