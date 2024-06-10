class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        n_heights = sorted(heights)
        count = 0

        for x, y in zip(n_heights, heights):
            if x != y:
                count += 1

        return count
