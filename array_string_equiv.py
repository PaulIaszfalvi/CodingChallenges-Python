class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        for c1, c2 in zip(self.gen(word1), self.gen(word2)):
            if c1 != c2:
                return False
        return True

    def gen(self, word):
        for s in word:
            for c in s:
                yield c
        # Ensure False when len(word1) != len(word2) 
        yield None
        
        

        # Solution 1
        # return ''.join(word1) == ''.join(word2)

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(Solution().arrayStringsAreEqual(word1, word2))