class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        #Second SOLUTION
        maximum = 0
        my_List = []

        for e in s:
            if e not in my_List:
                my_List.append(e)
            else:
                maximum = self.getLength(maximum, len(my_List))             
                my_List = my_List[my_List.index(e)+1:] + [e]            
                       
        maximum = self.getLength(maximum, len(my_List))

        return maximum

    def getLength(self, maximum, length_List):

        return max(maximum,length_List)
        #return maximum if maximum > length_List else length_List


        #FIRST SOLUTION
        # maximum = counter = 0
        # my_map = {}
        
        # for e in s:
        #     if e not in my_map:
        #         my_map[e] = my_map.get(e, 1)
        #         counter += 1                
        #     else:               
        #         maximum = maximum if maximum > counter else counter                               

        # maximum = maximum if maximum > counter else counter

        # return maximum


s = "abcabcbb"
s_1 = "bbbbb"
s_2 = "pwwkew"
s_3 = "aab"
s_4 = "dvdf"
s_5 = "aabaab!bb"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
print(sol.lengthOfLongestSubstring(s_1))
print(sol.lengthOfLongestSubstring(s_2))
print(sol.lengthOfLongestSubstring(s_3))
print(sol.lengthOfLongestSubstring(s_4))
print(sol.lengthOfLongestSubstring(s_5))