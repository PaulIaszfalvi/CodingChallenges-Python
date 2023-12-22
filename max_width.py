class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        # Slightly faster version is to use this sort
        # Since we only sort for x values, we don't care to sort the entire lists of lists, but the list by x's

        # points.sort(key=lambda x: x[0])

        # Solution 1

        # points.sort()
        # result = 0
        
        # for i in range(1, len(points)):

        #     result = max (points[i][0] - points[i-1][0], result)

        # return result