class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()  # Sort the positions
        
        # Binary search variables
        left, right = 1, position[-1] - position[0]
        n = len(position)
        
        def canPlace(distance):
            count = 1  # Start with placing the first element
            last_position = position[0]
            
            for i in range(1, n):
                if position[i] - last_position >= distance:
                    count += 1
                    last_position = position[i]
                    if count >= m:  # If we've placed all m elements
                        return True
            return False
        
        # Binary search for the maximum possible distance
        while left <= right:
            mid = (left + right) // 2
            if canPlace(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        # After the loop, right will be the largest distance that can be achieved with m elements
        return right
