class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Fastest online 
     
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

        # Solution 1
        
        d_s = {}
        d_t = {}

        for i, v in enumerate(s):
            indices = d_s.get(v, [])           
            indices.append(i)           
            d_s[v] = indices

        for i, v in enumerate(t):            
            indices = d_t.get(v, [])           
            indices.append(i)           
            d_t[v] = indices

        for (key1, value1), (key2, value2) in zip(d_s.items(), d_t.items()):
            if value1 == value2:
                continue
            else:
                return False

        return True