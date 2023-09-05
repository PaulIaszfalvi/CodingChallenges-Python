class Solution:
    def removeStars(self, s: str) -> str:
        
        # Solution 1

        # iterator = len(s)-1
        # counter = 0
        # result = ""

        # while iterator >= 0:
        #     print(s[iterator])
        #     if s[iterator] == "*":
        #         counter += 1
        #         print("found a star")
        #     elif counter > 0:
        #             counter -= 1
        #             print("skipped this")
        #     else:
        #         result = s[iterator] + result
        #         print("added result")

        #     iterator -= 1

        # return result

        # Solution 2

        stack = []

        for e in s:
            if e != "*":
                stack.append(e)
            else:
                stack.pop()

        return "".join(stack)


s = "leet**cod*e"
print(Solution().removeStars(s))