class Solution:
    def longestCommonPrefix(self, strs):
       list =[""]
       
        #sort by length
        self.strs = sorted(strs, key=len)

        prefix = ""
        update_prefix = False
        n1 = 0
        n2 = 1

        self.strs = list(zip(*strs))
        print(strs)

        if len(self.strs) == 1:
            return self.strs[0]
        elif len(self.strs[0]) <= 1:
            return self.strs[0] 

        for x in range(len(self.strs[0])):
            prefix = strs[0][n1: n2+1]
            #print(prefix)
            for item in strs:
                if prefix in item:                    
                    update_prefix = True
                else:
                    n2 -= 1
                    update_prefix = False
                    break

            if update_prefix:
                n2 += 1 
        
        return prefix

   

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))