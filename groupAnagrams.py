class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}

        for x in strs:
            y = ''.join(sorted(x))
            
            if y in ans:
                ans[y].append(x)
            else:
                ans[y] = [x]
        
        return list(ans.values())