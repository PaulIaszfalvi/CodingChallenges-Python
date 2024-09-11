class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        # Solution 2

        # Compute the XOR of start and goal
        diff = start ^ goal
        
        # Count the number of set bits (1s) in the result
        count = 0
        while diff:
            count += diff & 1
            diff >>= 1
        
        return count

        # Solution 1
        
        # Convert integers to binary strings without the '0b' prefix
        s = bin(start)[2:]
        g = bin(goal)[2:]

        # Pad the shorter binary string with leading zeros
        max_length = max(len(s), len(g))
        s = s.zfill(max_length)
        g = g.zfill(max_length)

        # Count the number of differing bits
        count = 0
        for i in range(max_length):
            if s[i] != g[i]:
                count += 1

        return count
