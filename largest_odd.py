class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        # Solution 2b
        for i in range(len(num) - 1, -1, -1) :
            if num[i] in {'1','3','5','7','9'} :
                return num[:i+1]
        return ''

        # Solution 2
        # n = len(num)

        # for i in range(n - 1, -1, -1):
        #     if int(num[i]) % 2 != 0:
        #         return num[:i + 1]

        # return ""

        # Solution 1
        # num = int(num)

        # if num % 2 != 0:
        #     return str(num)
        
        # while num > 0:
        #     num = num // 10
        #     if num % 2 != 0:
        #         return str(num)
        
        # return ""

        # Cool stuff from online

        return num.rstrip("02468")