class Solution:
    def plusOne(self, digits):

        digit = ""

        for s in digits:
            digit += str(s)

        digit = int(digit) + 1

        digits = [int(i) for i in str(digit)]

        return digits


digits = [9]
print(Solution().plusOne(digits))
digits = [1,2,3,4]
print(Solution().plusOne(digits))