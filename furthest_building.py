class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        # Solution 2

        min_heap = []  # min heap to store the height differences
        total_bricks_used = 0
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:  # need to use bricks or ladder
                heapq.heappush(min_heap, diff)
                
                if len(min_heap) > ladders:  # used all ladders
                    total_bricks_used += heapq.heappop(min_heap)
                
                if total_bricks_used > bricks:  # used all bricks
                    return i
        
        return len(heights) - 1  # reached the end

        # Solution 1
        
        for i in range(len(heights)-1):
            c = heights[i]
            n = heights[i+1]

            if c == n:
                continue
            elif c > n and bricks != 0:
                bricks -= (c-n)
                if bricks < 0: break
            elif c < n and ladders != 0:
                ladders -= 1
                if ladders < 0: break
            else:
                break

        return heights[i]