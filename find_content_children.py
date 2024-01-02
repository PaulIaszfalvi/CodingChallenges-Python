class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        
        result = c_g = c_s = 0

        while c_s < len(s) and c_g < len(g):

            if g[c_g] <= s[c_s]:
                result += 1
                c_g += 1
            c_s += 1

        return result
