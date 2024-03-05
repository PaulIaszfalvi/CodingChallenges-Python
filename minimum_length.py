class Solution:
    def minimumLength(self, s: str) -> int:
        b = 0
        e = len(s) - 1

        # Loop to trim equal characters from both ends
        while b < e and s[b] == s[e]:
            char = s[b]
            # Trim from the beginning
            while b <= e and s[b] == char:
                b += 1
            # Trim from the end
            while e >= b and s[e] == char:
                e -= 1

        # If b > e, it means all characters are trimmed, so return 0
        if b > e:
            return 0
        else:
            # Return the length of the remaining substring
            return e - b + 1
