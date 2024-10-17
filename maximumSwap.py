class Solution:
    def maximumSwap(self, num: int) -> int:

        # Solution 2

        num = list(str(num))  
        last = {int(x): i for i, x in enumerate(num)}  
        
      
        for i in range(len(num)):
            # Check for a larger digit that comes after the current digit
            for d in range(9, int(num[i]), -1):  # Start checking from 9 down to current digit + 1
                if last.get(d, -1) > i:  # If a larger digit appears after the current position
                    # Swap the current digit with the later larger digit
                    num[i], num[last[d]] = num[last[d]], num[i]
                    # Return the maximum swapped number as an integer
                    return int(''.join(num))
        
        # If no swap is made, return the original number
        return int(''.join(num))

        # Solution 1 (incomplete, passes 56 test cases)

        num = list(str(num))
        
        for i in range(1, len(num)):
            if num[i] > num[i-1]:
                num[i], num[i-1] = num[i-1], num[i]
                break

        return int(''.join(num))
