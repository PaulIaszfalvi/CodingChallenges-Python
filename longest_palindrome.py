class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        map = {}
        pivot = 0
        result = 0
        
        for e in s:
        
            map[e] = map.get(e, 0) +1
        
        for key, value in map.items():
            
            result += (value // 2) * 2 
            
            if pivot != 1:
                pivot = 1 if value % 2 > 0 else 0
            
        return result + pivot
    
