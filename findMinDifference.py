class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def getTime(t):
            return int(t[:2]) * 60 + int(t[3:])
        
        # Convert time points to minutes and sort them
        minutes = sorted(getTime(t) for t in timePoints)
        
        # Initialize minimum difference to a large value
        min_diff = float('inf')
        
        # Calculate the minimum difference between consecutive time points
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Also need to consider the difference between the last and first time point
        min_diff = min(min_diff, 1440 - (minutes[-1] - minutes[0]))
        
        return min_diff
