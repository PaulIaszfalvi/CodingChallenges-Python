class Solution:
    def frequencySort(self, s: str) -> str:

        # Solution 2 (Slightly optimized)

        d = {}
        
        for x in s:
            d[x] = d.get(x ,0) + 1

        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        
        return ''.join(key * value for key, value in sorted_dict.items())


        
        #Solution 1
    
        d = {}
        ans = ''

        for x in s:
            d[x] = d.get(x ,0) + 1

        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        
        for key, value in sorted_dict.items():          
            ans += key * value 

        return ans



















 

        