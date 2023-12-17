class Solution:
    def destCity(self, p: List[List[str]]) -> str:
source = set()
        dest = set()
        for l in p:
            source.add(l[0])
            dest.add(l[1])
        return list(dest - source)[0]
        # Sets (easiest)

        start = set()
        end = set()

        for l in p:
            start.add(l[0])
            end.add(l[1])
        return list(end - start)[0]
              
        # Solution 2
        p = sorted(p, key=lambda x: x[1])
              
        return p[-1][1]
        
        # Solution 1
        # start = p[0][0]
        # end = [p[0][1]]
      
        # for i in p:
        #     if i[0] in end or i[1] in end:
        #         end.append(i[1])
                
        # print(end)
        # return end[-1]