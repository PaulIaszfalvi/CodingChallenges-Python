class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # Solution 3 

        d = {}

        for x in arr:
            d[x] = d.get(x, 0) + 1

        d = sorted(d.items(), key=lambda x: x[1])
  
        i = 0
        while k > 0 and i < len(d):
            if k >= d[i][1]:
                k -= d[i][1]
                i += 1
            else:
                break

        return len(d)-i

        # Solution 2

        arr.sort()

        return len(set(arr[k:]))


        # Solution 1

        d = {}

        for x in arr:
            d[x] = d.get(x, 0) + 1

        s = sorted(d.items(), key=lambda x: x[1])
  
        for x in s:
            
            if k >= x[1]:
                k -= x[1]
                del d[x[0]]      
            

        return len(d)