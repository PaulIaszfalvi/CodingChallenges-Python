class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        # Slightly faster version is to use this sort

        # points.sort(key=lambda x: x[0])

        # Solution 1

        # points.sort()
        # result = 0
        
        # for i in range(1, len(points)):

        #     result = max (points[i][0] - points[i-1][0], result)

        # return result