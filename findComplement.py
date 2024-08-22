class Solution:
    def findComplement(self, num: int) -> int:

        # Solution 3

        # Handle edge case for num = 0
        if num == 0:
            return 1
        
        # Compute the bitmask with all bits set to 1 for the length of num
        bitmask = (1 << num.bit_length()) - 1
        
        # XOR num with the bitmask to get the complement
        return bitmask ^ num

        # Solution 2
        # Convert number to binary string and remove '0b' prefix
        binary = bin(num)[2:]
        
        # Calculate the complement by flipping each bit
        complement = ''.join('1' if x == '0' else '0' for x in binary)
        
        # Convert the complement binary string back to an integer
        return int(complement, 2)

        # Solution 1
        
        binary = bin(num)[2:]

        result = ''

        for x in binary:
            print(x)
            if x == '0':
                result += '1'
            else:
                result += '0'

        return int(result, 2)
