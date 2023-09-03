class Solution:
    def countBits(self, n: int):

        answer = []
        
        for e in range(0, n+1):

            answer.append((list(bin(e)[2:]).count('1')))

        return answer


sol = Solution()

n=2
print(sol.countBits(n))
n=5
print(sol.countBits(n))