class Solution:
    def minimumLength(self, s: str) -> int:
        
        d = Counter(s)
        ans = 0

        for i, v in d.items():
            while v >= 3:
                v -= 2
            ans += v

        return ans

        
