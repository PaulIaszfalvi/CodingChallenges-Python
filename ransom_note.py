class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        noteMap = {}        
        magazineMap = {}
         
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        
        for e in ransomNote:
            noteMap[e] = noteMap.get(e, 0) +1
        
        for e in magazine:
            magazineMap[e] = magazineMap.get(e, 0) +1
            
        for key, values in noteMap.items():
            
            num_in_magazine = magazineMap.get(key)

            if num_in_magazine == None or num_in_magazine < values:                         
                return False
            
        return True

note = "aa"
magazine="aab  "
sol = Solution()
print(sol.canConstruct(note, magazine))

# def canConstruct(self, ransomNote, magazine):
#         for i in set(ransomNote):
#             if magazine.count(i) < ransomNote.count(i):
#                 return False
#         return True