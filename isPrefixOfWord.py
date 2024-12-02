class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        # Solution 2

        arr = list(sentence.split())
        
        for i, v in enumerate(arr):
        
            if searchWord == v[0 : len(searchWord)]:
                return i+1
            
        return -1


        # Solution 1

        arr = list(sentence.split())
        
        for i, v in enumerate(arr):
        
            if searchWord in v and searchWord == v[0 : len(searchWord)]:
                return i+1
            
        return -1
