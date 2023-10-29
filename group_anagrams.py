from ast import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs):
        
        anagram_groups = {}

        for word in strs:
            # Sort the characters in the word
            sorted_word = ''.join(sorted(word))
            
            # Check if the sorted word is in the dictionary
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        return list(anagram_groups.values())
    

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

strs = ["","",""]
print(Solution().groupAnagrams(strs))