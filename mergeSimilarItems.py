class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        # Solution 1
        
        d = {}
        ans = []

        for x in items1:
            v1 = x[0]
            w1 = x[1]

            d[v1] = d.get(v1, 0) + w1

        for x in items2:
            v1 = x[0]
            w1 = x[1]

            d[v1] = d.get(v1, 0) + w1

        for x in d.items():
            ans.append([x[0], x[1]])

        return sorted(ans)

