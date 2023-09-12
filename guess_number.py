# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # Solution 1

        # lower = 1
        # upper = n
        
        # while True:

            # num = (lower + upper) // 2            
            # temp = guess(num)

            # if temp == -1:
            #     upper = num - 1
            # elif temp == 1:
            #     lower = num + 1
            # else:
            #     return num
                
        # Solution 2

        lower, upper, myGuess = 1, n, (n+1) // 2
   
        while guess(myGuess) != 0:
            if guess(myGuess) < 0:
                upper = myGuess - 1
            else:
                lower = myGuess + 1
            myGuess = (upper + lower) // 2
           # myGuess = (upper + lower) >> 1
        return myGuess
                



