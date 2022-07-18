class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
        
        map = {}
        
        s = self.split(s)
        t = self.split(t)
        
        for element in s:
            map[element] = map.get(element, 0) + 1 
            
        for element in t:
            map[element] = map.get(element, 0) - 1 
         
        for key, value in map.items():
            if value is not 0:
                return False        
            
        return True
        
    
    def split(self, string):
        
        return [char for char in string]
    


# import itertools


# class Solution(object):
#     def isAnagram(self, s, t):
        
#         if len(s) != len(t):
#             return False
        
#         chars = list(s)        
#         permutations = list(itertools.permutations(chars))
#         permutations = [''.join(permutation) for permutation in permutations]
               
#         return t in permutations
        
    

    
sol = Solution()
print(sol.isAnagram("ABCDEFGE", "ABCDFGEE"))