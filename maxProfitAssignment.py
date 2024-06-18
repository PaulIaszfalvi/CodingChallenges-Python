class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        # Solution 2

        n = len(difficulty)
        max_profit = 0
        current_max_profit = 0
        j = 0
        
        # Combine difficulty and profit and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        for ability in worker:
            # Move through jobs while they are suitable for the current worker's ability
            while j < n and jobs[j][0] <= ability:
                current_max_profit = max(current_max_profit, jobs[j][1])
                j += 1
            
            max_profit += current_max_profit
        
        return max_profit


        # Solution 1

        work = len(worker)
        max_profit = 0
        worker.sort()
        
        for ability in worker:
            b = 0
            while b < len(difficulty) and difficulty[b] <= ability:
                b += 1
            
            if b > 0:
                max_profit += max(profit[:b])
        
        return max_profit


       

       
