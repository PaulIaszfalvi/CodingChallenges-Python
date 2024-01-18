class Solution:
    def climbStairs(self, n: int) -> int:       

        # Fibonacci Sequence

        f, s = 0, 1

        for x in range(n):
            f, s = s, s + f
        
        return s
    
        # Using matrix multiplication to get the sequence
           
        # if n <= 1:
        #     return 1

        # def multiply(a, b):
        #     return [
        #         [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        #         [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        #     ]

        # def power(matrix, exp):
        #     result = [[1, 0], [0, 1]]
        #     while exp > 0:
        #         if exp % 2 == 1:
        #             result = multiply(result, matrix)
        #         matrix = multiply(matrix, matrix)
        #         exp //= 2
        #     return result

        # base_matrix = [[1, 1], [1, 0]]
        # result_matrix = power(base_matrix, n - 1)
        # return result_matrix[0][0] + result_matrix[0][1]
    
        # Same as above but recursive
    
        if n <= 1:
            return 1

        def multiply(a, b):
            return [
                [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
            ]

        def power(matrix, exp):
            if exp == 0:
                return [[1, 0], [0, 1]]
            if exp % 2 == 0:
                half_pow = power(matrix, exp // 2)
                return multiply(half_pow, half_pow)
            else:
                return multiply(matrix, power(matrix, exp - 1))

        base_matrix = [[1, 1], [1, 0]]
        result_matrix = power(base_matrix, n - 1)
        return sum(result_matrix[0])

