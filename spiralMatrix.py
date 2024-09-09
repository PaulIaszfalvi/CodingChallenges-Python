
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Initialize boundaries for the spiral
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        while top <= bottom and left <= right:
            # Fill top row
            for col in range(left, right + 1):
                if head:
                    matrix[top][col] = head.val
                    head = head.next
                else:
                    matrix[top][col] = -1
            top += 1
            
            # Fill right column
            for row in range(top, bottom + 1):
                if head:
                    matrix[row][right] = head.val
                    head = head.next
                else:
                    matrix[row][right] = -1
            right -= 1
            
            # Fill bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if head:
                        matrix[bottom][col] = head.val
                        head = head.next
                    else:
                        matrix[bottom][col] = -1
                bottom -= 1
            
            # Fill left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if head:
                        matrix[row][left] = head.val
                        head = head.next
                    else:
                        matrix[row][left] = -1
                left += 1
        
        return matrix
