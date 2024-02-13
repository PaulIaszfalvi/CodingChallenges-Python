class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def pal(s):           
            return s == s[::-1]

        for x in words:
            if pal(x):
                return x

        return ""