class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counts = [0] * 1024  # Bitmask to represent the parity of letter counts
        counts[0] = 1  # Empty string is wonderful
        
        bitmask = 0
        result = 0
        
        for char in word:
            idx = ord(char) - ord('a')
            bitmask ^= (1 << idx)  # Update bitmask
            
            # Update result with substrings ending at the current position
            result += counts[bitmask]
            
            # Check substrings with exactly one letter appearing odd times
            for i in range(10):
                result += counts[bitmask ^ (1 << i)]
            
            counts[bitmask] += 1
        
        return result
