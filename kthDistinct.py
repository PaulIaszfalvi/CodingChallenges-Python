class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

      # Solution 2

      counts = Counter(arr)
        
        distinct_count = 0
        for x in arr:
            if counts[x] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return x
        
        return ""

      # Solution 1

        d = {x:arr.count(x) for x in arr}
        c = 0

        for x in arr:
            if d[x] == 1:
                c += 1
                if c == k:
                    return x
        
        return ""
