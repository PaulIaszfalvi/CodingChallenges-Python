class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        #Solution 2 
        return max(n[i-2:i+1] if n[i] == n[i - 1] == n[i - 2] else "" for i in range(2, len(n)))

        # Solution 1
        # maximum = float('-inf')

        # for i in range(len(num)-2):
        #     if num[i] == num[i+1] == num[i+2]:
        #         maximum = max(int(num[i:i+3]), maximum)

        # return str(maximum) if maximum != float('-inf') else ""