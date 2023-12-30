class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        # Solution 1
        
        if len(s) < 2 and k > 0:
                return 0
        if len(s) - 1 == k:
            return 1

        s = list(s)
        s.sort()
        count = 1
        ans = []
        c = 0

        while c < len(s) - 1:
            if s[c] == s[c+1]:
                count += 1                
            else:
                ans.append(s[c])
                ans.append(count)
                count = 1
            c += 1

        if count > 1 or c == len(s) - 1:
            ans.append(s[-1])
            ans.append(count)

        while k > 0 and len(ans) > 1:
            min_count = min(ans[1::2])     
                 
            if k >= min_count:
                index = ans.index(min_count)
                del ans[index - 1: index + 1]
                k -= min_count
            else:
                break

        ans = [x for x in ans if x != 1]

        return len(''.join(map(str, ans)))
