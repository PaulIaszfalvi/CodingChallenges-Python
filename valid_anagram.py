class Solution(object):
    def isAnagram(self, s, t):
        # Solution 1
        
    #     if len(s) != len(t):
    #         return False
        
    #     map = {}
        
    #     s = self.split(s)
    #     t = self.split(t)
        
    #     print(s)
    #     print(t)

    #     for element in s:
    #         map[element] = map.get(element, 0) + 1 

    #     print(map)

    #     for element in t:
    #         map[element] = map.get(element, 0) - 1 
         
    #     for key, value in map.items():
    #         if value is not 0:
    #             return False        
            
    #     return True
        
    
    # def split(self, string):
        
    #     return [char for char in string]
        

# import itertools


# class Solution(object):
#     def isAnagram(self, s, t):
        
#         if len(s) != len(t):
#             return False
        
#         chars = list(s)        
#         permutations = list(itertools.permutations(chars))      
#         permutations = [''.join(permutation) for permutation in permutations]
#         print(permutations)
               
#         return t in permutations
        
        return sorted(list(s)) == sorted(list(t))

    
sol = Solution()
print(sol.isAnagram("abcd", "dbca"))

print(sol.isAnagram("anagram", "nagaram"))