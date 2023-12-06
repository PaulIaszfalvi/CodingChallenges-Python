class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        # points.sort()

        # Solution 3 based on Solution 2

        # return sum(max(abs(A[0] - B[0]), abs(A[1] - B[1])) for A, B in zip(points[:-1], points[1:]))

        # Solution 2

        def get_max(A, B):
            return max(abs(A[0] - B[0]), abs(A[1] - B[1]))
        
        ans = 0
        
        for tup1, tup2 in zip(points[:-1], points[1:]):
            ans += get_max(tup1, tup2)
        
        return ans
        
        # Solution 1
        # def distance(p1, p2):
        #     if p1[0] == p2[0]:
        #         return abs(p1[1] - p2[1])
        #     elif p1[1] == p2[1]:
        #         return abs(p1[0] - p2[0])                
        #     else:
        #         return ((p1[0] + p2[0])**2 + (p1[1] + p2[1])**2)**0.5 // 2**0.5
            

        # ans = 0
        # start = points[0]

        # for vals in points[1:]:           
        #     ans += distance(start, vals)
        #     start = vals

        # return ans

points = [[1,1],[3,4],[-1,0]]
print(Solution().minTimeToVisitAllPoints(points))

