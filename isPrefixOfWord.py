class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        arr = list(sentence.split())
        
        for i, v in enumerate(arr):
        
            if searchWord in v and searchWord == v[0 : len(searchWord)]:
                return i+1
            
        return -1
