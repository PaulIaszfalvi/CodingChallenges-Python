class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # Solution 2

        vowels = set("aeiou")
        v = sum(1 for x in s[:k] if x in vowels)
        max_vowels = v
        

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                v -= 1
            if s[i] in vowels:
                v += 1

            # max_vowels = max(max_vowels, v)
            # Assigns the value to max_vowels as above, but also checks
            # to see if we've reached the maximum vowels we can have
            # break early if so
            if (max_vowels := max(max_vowels, v)) == k:
                    break
   
        return max_vowels

        # Solution 1
        
        ans = 0
        vowels = "aeiou"
        
        for i in range(len(s) - k + 1):
            print(ans, i, k, s[i:i+k])
            ans = max(ans, sum(1 for x in s[i:i+k] if x in vowels))

        return ans