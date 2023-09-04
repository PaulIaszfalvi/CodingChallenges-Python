class Solution:
    def reverseVowels(self, s: str) -> str:
        
        #vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        vowels = "aeiouAEIOU"
        s = list(s)

        front = 0
        back = len(s)-1

        while front < back:

            if s[front] in vowels and s[back] in vowels:
                s[front], s[back] = s[back], s[front]
                front += 1
                back -= 1

            elif s[front] not in vowels:
                front += 1

            elif s[back] not in vowels:
                back -= 1

        return "".join(s)





s = "hello"
print(Solution().reverseVowels(s))

s = "leetcode"
print(Solution().reverseVowels(s))