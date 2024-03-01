class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        # Solution 4

        one = 0
        l = len(s)

        for x in s:
            if x == '1':
                one += 1
           
        zero = len(s) - one

        if one == 1:
            return '0' * zero + '1'
        else:           
            return '1' * (one - 1) + '0' * zero + '1'
            

        # Solution 3

        one, zero = 0, 0
        l = len(s)

        for x in s:
            if x == '1':
                one += 1
            else:
                zero += 1

        if one == 1:
            return '0' * zero + '1'
        else:           
            return '1' * (one - 1) + '0' * zero + '1'

        # Solution 2

        one, zero = 0, 0
        l = len(s)

        for x in s:
            if x == '1':
                one += 1
            else:
                zero += 1

        if one == 1:
            return ''.join(['0' * (l - 1), '1']) 
        else:
            one -= 1
            s = ''.join(['1' * one, '0' * zero])
            return ''.join([s, '1'])

        # Solution 1
        
        c = 0
        l = len(s)

        for x in s:
            if x == '1':
                c += 1

        if c == 1:
            return ''.join(['0' * (l - 1), '1']) 
        else:
            c -= 1
            s = ''.join(['1' * c, '0' * (l - c - 1)])
            return ''.join([s, '1'])