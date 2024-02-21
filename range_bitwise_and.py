class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # Solution 1
        
        shift = 0
        
        # Find the common prefix length by right shifting until left and right are equal
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Left shift the common prefix to obtain the final result
        return left << shift