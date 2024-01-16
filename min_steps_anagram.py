class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # Solution 1 (Best even compared to the others online)
        
        count = 0
        s_d = t_d = {}
        
        for x in s:
            s_d[x] = s_d.get(x, 0) + 1

        for x in t:
            t_d[x] = t_d.get(x, 0) + 1


        for x in s_d:
            if t_d.get(x):
                s_d[x] = s_d.get(x) - t_d.get(x) 
            if s_d.get(x) >= 0:
                count += abs(s_d.get(x))

        return count 