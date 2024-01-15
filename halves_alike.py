class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        # Solution 2
       
        vowels = set("AEIOUaeiou")
        
        a = s[:len(s)//2]
        b = s[len(s)//2:]

        count_a = sum(1 for x in a if x in vowels)
        count_b = sum(1 for x in b if x in vowels)

        return count_a == count_b
    
        # Solution 1 b
        # def getCount(string):
        #         vowels = "AEIOUaeiou"
        #     return sum(1 for x in string if x in vowels)

        # a = s[:len(s)//2]
        # b = s[len(s)//2:]

        return getCount(a) == getCount(b)
    
        # Solution 1
           
        # def getCount(string):
        #     vowels = "AEIOUaeiou"
        #     count = 0

        #     for x in string:
        #          if x in vowels:
        #              count += 1

        #     return count

        # a = s[:len(s)//2]
        # b = s[len(s)//2:]

        # return getCount(a) == getCount(b)