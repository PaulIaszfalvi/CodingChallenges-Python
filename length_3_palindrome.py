class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        # Solution 2 

        def is_palindrome(subsequence):
            return subsequence == subsequence[::-1]

        def generate_palindromic_subsequences(index, current_subsequence=""):
            if len(current_subsequence) == 3:
                return [current_subsequence] if is_palindrome(current_subsequence) else []

            if index == len(s):
                return []

            include_current = generate_palindromic_subsequences(index + 1, current_subsequence + s[index])
            exclude_current = generate_palindromic_subsequences(index + 1, current_subsequence)

            return include_current + exclude_current

        palindromic_subsequences = set(generate_palindromic_subsequences(0))
        

        return len(palindromic_subsequences)

        # Solution 1
        
        # def is_palindrome(subsequence):
        #     return subsequence == subsequence[::-1]

        # def generate_subsequences(index, current_subsequence=""):
        #     if index == len(s):
        #         return [current_subsequence] if is_palindrome(current_subsequence) else []

        #     include_current = generate_subsequences(index + 1, current_subsequence + s[index])
        #     exclude_current = generate_subsequences(index + 1, current_subsequence)

        #     return include_current + exclude_current

        # palindromic_subsequences = set(generate_subsequences(0))
   
        # return len([x for x in palindromic_subsequences if len(x) == 3])


s = "aabca"
print(Solution().countPalindromicSubsequence(s))

# Online Solution 

# min_exist = [float('inf')] * 26
#         max_exist = [float('-inf')] * 26
#         unique_count = 0

#         for i, char in enumerate(s):
#             char_index = ord(char) - ord('a')
#             min_exist[char_index] = min(min_exist[char_index], i)
#             max_exist[char_index] = max(max_exist[char_index], i)

#         for char_index in range(26):
#             if min_exist[char_index] != float('inf') and max_exist[char_index] != float('-inf'):
#                 unique_count += len(set(s[min_exist[char_index] + 1 : max_exist[char_index]]))

#         return unique_count