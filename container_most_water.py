class Solution:
    def maxArea(self, height) -> int:

        # Solution 1

        # def findGreater(column, pointer):
        #     if height[column] > height[pointer]:
        #         return column
        #     return pointer
        
        # area, left, right, colLeft, colRight = 0, 0, len(height)-1, 0, len(height)-1

        # while left < right:

        #     colLeft = findGreater(colLeft, left)
        #     colRight = findGreater(colRight, right)
           
        #     currentArea = min(height[colLeft], height[colRight]) * (colRight - colLeft)
        #     area = max(area, currentArea)
        #     left += 1
        #     right -= 1
        #     print(colLeft, colRight, height[colLeft], height[colRight], currentArea)
        # return area
    
        # Solution 2

        left, right, maxArea = 0, len(height)-1, 0

        while left < right:

            curArea = min(height[left], height[right]) * (right - left)
            maxArea = max(curArea, maxArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea



height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
height = [1,1]
print(Solution().maxArea(height))
height = [2, 1]
print(Solution().maxArea(height))
height = [1,2,4,3]
print(Solution().maxArea(height))