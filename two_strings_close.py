from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        # Solution 1
        # mapOne = {}
        # mapTwo = {}

        # for w in word1:
        #     mapOne[w] = mapOne.get(w, 0) + 1

        # for w in word2:
        #     mapTwo[w] = mapTwo.get(w, 0) + 1

        # for i in mapOne:
        #     if mapOne.get(i) != mapTwo.get(i):
        #         return False
            
        # return True

        # Solution 2

        # if len(word1) != len(word2):
        #     return False

        # if set(word1) != set(word2):
        #     return False

        # if list(word1).sort() != list(word2).sort():
        #     return False

        # return True

        return len(word1) == len(word2) \
            and set(word1) == set(word2) \
            and Counter(Counter(word1).values()) == Counter(Counter(word2).values())


word1 = "abc"
word2 = "bca"

print(Solution().closeStrings(word1, word2))

word1 = "a"
word2 = "aa"

print(Solution().closeStrings(word1, word2))