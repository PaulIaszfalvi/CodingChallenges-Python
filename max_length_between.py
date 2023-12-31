class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        # Solution 3 with optimization

        f_chars = {}
        longest = -1
      
        for l in range(len(s)):

            if s[l] in f_chars:
                longest = max(longest, l - f_chars[s[l]] - 1)
            else:               
                f_chars[s[l]] = l
                
        return longest

        # Solution 2

        # if len(set(s)) == len(s):
        #     return -1

        # f_chars = {}  
        # longest = 0
      
        # for l, char in enumerate(s):

        #     if char not in f_chars:
        #         f_chars[char] = l
        #     else:               
        #         longest = max(longest, l - f_chars[char] - 1)

        # return longest



        # Solution 1 two pointers

        # if len(set(s)) == len(s):
        #     return -1
        
        # longest = 0
        # f_chars = l_chars = {}
        # f, l = 0, len(s)-1

        # while f < l:
        #     if s[f] not in f_chars:
        #         f_chars[s[f]] = f
            
        #     if s[l] not in l_chars:
        #         l_chars[s[l]] = l

        #     if s[f] in l_chars or s[l] in f_chars:
        #         # Check if s[l] is in f_chars before accessing it
        #         if s[l] in f_chars:
        #             longest = max(longest, l - f_chars[s[l]] - 1)

        #         # Check if s[f] is in l_chars before accessing it
        #         if s[f] in l_chars:
        #             longest = max(longest, l_chars[s[f]] - f - 1)

        #         # Now you can update f_chars and l_chars
        #         if f_chars.pop(s[l], None) is not None:
        #             l_chars.pop(s[l], None)
        #         else:
        #             f_chars.pop(s[f], None)
        #             l_chars.pop(s[f], None)

        #     f += 1
        #     l -= 1
        
        # return longest