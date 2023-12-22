class Solution:
    def maxScore(self, s: str) -> int:
        # Soluion 1

        zeroes = 0
        ones = s.count('1')
        maximum = 0

        for i in range(len(s) - 1):
            zeroes += s[i] == '0'
            ones -= s[i] == '1'

            maximum = max(maximum, zeroes + ones)            

        return maximum

        # Solution if we were looking for biggest binary values

        # maximum = 0

        # for i in range(1, len(s)-1):
        #     val = int(s[:i], 2) + int(s[i:], 2)
        #     maximum = max(val, maximum)

        # return maximum
