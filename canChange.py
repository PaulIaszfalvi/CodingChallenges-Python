class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove underscores and check if the order of L and R characters matches
        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        # Two pointers to check the positions of L and R
        j = 0
        for i in range(len(start)):
            if start[i] == "_":
                continue
            while target[j] == "_":
                j += 1
            # Check rules for L and R
            if (start[i] == "L" and i < j) or (start[i] == "R" and i > j):
                return False
            j += 1
        
        return True
