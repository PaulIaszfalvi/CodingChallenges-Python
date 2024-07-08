class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        # Solution 2
        winner = 0  # Base case: for n = 1, the winner is index 0
        
        # Iterate through each number from 2 to n to find the position
        for i in range(1, n + 1):
            winner = (winner + k) % i

        # Return the winner position adjusted to 1-based index
        return winner + 1

        # Solution 1
        
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
