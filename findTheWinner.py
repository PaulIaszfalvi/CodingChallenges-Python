class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Create a list of participants
        l = [x for x in range(1, n + 1)]
        pos = 0

        # Loop until only one participant remains
        while len(l) > 1:
            # Calculate the position of the next person to be removed
            pos = (pos + k - 1) % len(l)
            l.pop(pos)

        # Return the last remaining participant
        return l[0]
