class Solution:
    def sortVowels(self, s: str) -> str:
        vow = 'aeiouAEIOU'
        vow_chars = [char for char in s if char in vow]
        sorted_vowels = sorted(vow_chars, key=lambda x: ord(x))

        result = ''
        j = 0

        for x in s:
            if x in vow:
                result += sorted_vowels[j]
                j += 1
            else:
                result += x

        return result
