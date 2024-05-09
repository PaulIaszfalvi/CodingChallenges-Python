class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()
        ans = 0

        for i in range(k):
            if happiness[-1 - i] - i > 0:
                ans += happiness[-1 - i] - i
            else:
                pass

        return ans