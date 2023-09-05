class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        #Solution 1

        # arrDict = {}

        # for e in arr:
        #     arrDict[e] = arrDict.get(e, 0) + 1

        # mySet = set(arrDict.values())
        
        # return len(mySet) == len(set(arr))
    
        # Solution 2

        arrDict = {}

        for e in arr:
            arrDict[e] = arrDict.get(e, 0) + 1

        mySet = set()

        for val in arrDict.values():
            if val in mySet:
                return False
            else:
                mySet.add(val)
                
        return True

            
arr = [1,2,2,1,1,3]
print(Solution().uniqueOccurrences(arr))

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(Solution().uniqueOccurrences(arr))