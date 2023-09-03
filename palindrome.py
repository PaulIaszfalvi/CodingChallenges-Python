class Solution(object):
    def isPalindrome(self, s):  
     
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        
        reverse = s[::-1]
    
        return s == reverse

pal = "A man, a plan, a canal: Panama"

palindrome = Solution()
print(palindrome.isPalindrome(pal))