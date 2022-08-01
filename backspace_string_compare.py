class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.remove(s) == self.remove(t)
        
    def remove(self, s) -> str:
        
        my_str = ''
        
        for e in s:
            my_str = my_str + e if e is not '#' else my_str[:-1]
            
        return my_str

s = "ab##"
t = "c#d#"

sol = Solution()
print(sol.backspaceCompare(s, t))