from ast import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        newList = []
        output = []
                
        
        for e in points:
            newList.append([self.getLength(e[0], e[1]), e])
        
        newList.sort()
        
        for i in range(k):           
            output.append(newList[i][1])
        
        return output
            
    def getLength(self, x, y):
        
        return (x ** 2 + y ** 2) ** .5


    # Cool solution

    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     points.sort(key = lambda P:P[0]**2+P[1]**2)
    #     return points[:K]


        