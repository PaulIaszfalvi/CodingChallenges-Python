class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Solution 2
    
        s = s.strip()  # Trim leading and trailing spaces
        if not s:  # If the string is empty after trimming, return 0
            return 0
        return len(s.split()[-1])  # Return the length of the last word


        # Solution 1
              
        return len(s.split()[-1])