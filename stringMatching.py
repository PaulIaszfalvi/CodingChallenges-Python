from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)  
        full_text = " ".join(words) 
        return [w for w in words if full_text.count(w) > 1]  
