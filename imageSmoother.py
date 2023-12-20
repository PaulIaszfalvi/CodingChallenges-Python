class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        # Solution 1
        
        # def adjacents(i, j):
        #     count, s = 0, 0

        #     for x in range(i - 1, i + 2):
        #         for y in range(j - 1, j + 2):
        #             if 0 <= x < len(img) and 0 <= y < len(img[0]):
        #                 s += img[x][y]
        #                 count += 1

        #     return s // count if count else 0

        # result = []

        # for i in range(len(img)):
        #     row = []
        #     for j in range(len(img[0])):
        #         row.append(adjacents(i, j))
        #     result.append(row)

        # return result

        # Online best solution

        # rows, cols = len(img), len(img[0])
        # result = [[0] * cols for _ in range(rows)]

        # for i in range(rows):
        #     for j in range(cols):
        #         total_sum = 0
        #         count = 0

        #         for x in range(max(0, i-1), min(rows, i+2)):
        #             for y in range(max(0, j-1), min(cols, j+2)):
        #                 total_sum += img[x][y]
        #                 count += 1

        #         result[i][j] = total_sum // count

        # return result