class Solution(object):
    def mergeAlternately(self, word1, word2):

        # String is faster, but we have to create a new string every time we concatonate.
        
        len1 = len(word1)
        len2 = len(word2)
        #result = ""
        result = []

        for i in range(max(len1, len2)):
            if i < len1:
            #     result += word1[i]
                result.append(word1[i])
            if i < len2:
            #     result += word2[i] 
                result.append(word2[i])               
           

        return "".join(result)      
        
           
word1 = "abc"
word2 = "pqr"

print(Solution().mergeAlternately(word1, word2))

word1 = "ab"
word2 = "pqrs"

print(Solution().mergeAlternately(word1, word2))