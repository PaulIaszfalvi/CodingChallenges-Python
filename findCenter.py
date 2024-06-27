class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        # Solution 2

        if edges[1][0] == edges[0][0] or edges[1][1] == edges[0][0]:
            return edges[0][0]
        
        else:
            return edges[0][1]

        # Solution 1
        
        d = {}
        result = edges[0][0]

        for x in edges:
            d[x[0]] = d.get(x[0], 0) + 1
            d[x[1]] = d.get(x[1], 0) + 1

        for x, y in d.items():
            result = result if d.get(result) > y else x

        return result
