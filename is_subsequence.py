class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Solution 1

        # first = 0
        # second = 0

        # while first < len(s):
            
        #     if second >= len(t):
        #         return False
            
        #     if s[first] == t[second]:
        #         first += 1                

        #     second += 1

        # return True

        # Solution 2
        if not s:
            return True
        
        count = 0

        for i in t:

            if i == s[count]:
                count += 1

            if count == len(s):
                break

        return len(s) == count



s = "abc"
t = "ahbgdc"

print(Solution().isSubsequence(s, t))

s = "axc"
t = "ahbgdc"

print(Solution().isSubsequence(s, t))