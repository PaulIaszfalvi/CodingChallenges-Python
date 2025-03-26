from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = sorted([num for row in grid for num in row])
        median = flattened[len(flattened) // 2]  # Choose median as the target
        operations = 0

        for num in flattened:
            diff = abs(num - median)
            if diff % x != 0:  # If difference isn't a multiple of x, impossible
                return -1
            operations += diff // x

        return operations  # Ensure function returns result
