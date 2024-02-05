class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for x in s:
            d[x] = d.get(x, 0) + 1

        for i, v in enumerate(s):
            if d[v] == 1:
                return i
        
        return -1