class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        c = 0
        l = len(pref)

        for w in words:
            if w[:l] == pref:
                c += 1

        return c
