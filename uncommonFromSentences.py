class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      # Solution 2

        w1 = s1.split()
        w2 = s2.split()

        count = Counter(w1 + w2)

        return [w for w in count if count[w] == 1]
  
      # Solution 1
        
        d1, d2 = {}, {}
        ans = []

        for x in s1.split(' '):
            d1[x] = d1.get(x, 0) + 1
        
        for x in s2.split(' '):
            d2[x] = d2.get(x, 0) + 1

        for y in d1:
            if d1[y] == 1 and y not in d2:
                ans.append(y)

        for y in d2:
            if d2[y] == 1 and y not in d1:
                ans.append(y)

        return ans
