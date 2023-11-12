class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, cols - 1  # Start from the top-right corner

        while i < rows and j >= 0:
            position = matrix[i][j]

            if target == position:
                return True
            elif target < position:
                j -= 1  # Move left
            else:
                i += 1  # Move down

        return False
