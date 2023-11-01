class Solution:
    def convert(self, s: str, numRows: int) -> str:

         # Best Solution

        result = [[] for _ in range(numRows)]
        index = 0

        if numRows == 1 or numRows >= len(s):
            return s

        for char in s:

            result[index].append(char)

            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1

            index += step

        for i in range(numRows):
            result[i] = ''.join(result[i])

        return ''.join(result)

        # First solution
        
        # ans = [[] for _ in range(numRows)]
        # index = 0
        # down = True
        # result = []

        # if numRows == 1:
        #     return s

        # for char in s:
        #     ans[index].append(char)
            
        #     if down:
        #         index += 1
        #     else:
        #         index -= 1

        #     if index == numRows:
        #         index -= 2
        #         down = False
        #     if index == 0:
        #         down = True

        # for arr in ans:            
        #     result.extend(arr)
        
        # return "".join(result)


      


s = "PAYPALISHIRING"
numRows = 4
#Output: "PINALSIGYAHRPI"
print(Solution().convert(s, numRows))