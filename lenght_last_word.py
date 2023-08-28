class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip()
        count = 0

        for i in s[::-1]:
            if i == " ":
                break
            count += 1

        return count
       #return len(list(s.split())[-1])