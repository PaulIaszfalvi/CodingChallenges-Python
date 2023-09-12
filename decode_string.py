class Solution:
    def decodeString(self, s: str) -> str:
        
        # # Solution 1

        # stack = []
        # result = []
        # temp = ""
                
        # for e in s:  
         
        #     if e.isnumeric():
        #         mult = e
        #     elif e == "[":
        #         stack.append(e)
        #         temp = ""
        #     elif e == "]":
        #         while stack[len(stack)-1] != "[":
        #             temp += stack.pop()
        #         result.append(int(mult) * temp)
        #         stack.pop()
        #     else:
        #         stack.append(e)
         

        # return "".join(result) + "".join(stack)


        # Solution 2

        stack = []

        for e in s:
            stack.append(e)

        while len(stack) - 1 >= 0:

            pass
        
                






s = "3[a]2[bc]"
print(Solution().decodeString(s))

s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))