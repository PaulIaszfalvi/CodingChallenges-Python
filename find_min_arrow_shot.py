class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # Solution 2

        if not points:
            return 0
        
        # Sort intervals based on their end points
        points.sort(key=lambda x: x[1])
        
        # Initialize variables
        arrows = 1
        end = points[0][1]
        
        # Iterate through intervals
        for start, point_end in points:
            # If the current interval's start point is greater than end,
            # it's a non-overlapping range, so increment arrows count
            if start > end:
                arrows += 1
                end = point_end  # Update end point
            
        return arrows


        # Solution 1
        
        def merge(points):
            n_l = [points[0]]

            for i in range(1, len(points)):
                if n_l[-1][1] >= points[i][0]:
                    n_l[-1][1] = min(n_l[-1][1], points[i][1])
                else:
                    n_l.append(points[i])
                
            
            return n_l

        points.sort(key=lambda x: x[0])

        return len(merge(points))