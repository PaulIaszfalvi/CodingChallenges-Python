class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        ans = []
        d = {h:n for h, n in zip(heights, names)}
        sorted_d = dict(sorted(d.items(), reverse=True))          
       
        for n in sorted_d.items():
            ans.append(n[1])

        return ans
