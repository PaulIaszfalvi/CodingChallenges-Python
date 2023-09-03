class Solution:
    def romanToInt(self, s: str) -> int:

        previous = 0
        head = 0
        total = 0

        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        print(s)

        for x in s[::-1]:
            temp = values.get(x)
            #Reset if value is greater than last one
            if previous < temp:
                head = 0
            #Set the head to check when the values are smaller we subtract   
            if temp >= head:
                head = temp
                total += head
            else:
                total -= temp
            previous = temp
            #print(x, temp)

        return total


# Cool alternative 

# class Solution:
#     def romanToInt(self, s: str) -> int:
\
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number