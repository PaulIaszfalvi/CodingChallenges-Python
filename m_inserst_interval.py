from ast import List

class Solution:
    def insert(self, intervals, newInterval):


        newList = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                newList.append(newInterval)
                return newList + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                newList.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        newList.append(newInterval)
        
        return newList

        # start = newInterval[0]
        # end = newInterval[1]

        # newList = []
        # nothing_to_do = False

        # if len(intervals) is 0:
        #     newList.append(newInterval)   
        # else: 
        # # Merge all items into a list before adding it to the new list. Keep movving the start and end until they no longer fit into a list, then add the smallest start with the largest end
        #     for interval in intervals:        

        #         if interval[0] <= start <= interval[1]:
        #             start = start if start <= interval[0] else interval[0]           
        #         if interval[0] <= end:
        #             end = end if end >= interval[1] else interval[1]    

        
        #     for interval in intervals: 

        #         if start > interval[1] or end < interval[0]:
        #             newList.append(interval)
        #         elif [start, end] not in newList:
        #             newList.append([start, end])       

        return newList




intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals_1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval_1 = [4,8]

intervals_2 = [[1,5]]
newInterval_2 = [2,3]

intervals_3 = [[1,5]]
newInterval_3 = [6,8]

sol = Solution()
print(sol.insert(intervals, newInterval))
print(sol.insert(intervals_1, newInterval_1))
print(sol.insert(intervals_2, newInterval_2))
print(sol.insert(intervals_3, newInterval_3))

