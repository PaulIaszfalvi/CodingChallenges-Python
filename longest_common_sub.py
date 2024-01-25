class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # DP Solution (Online)
        
        m, n = len(text1), len(text2)

        # Initialize a 2D array to store the length of LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp array using dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]



        # Solution 4 (time exceeded) O(2^n)

        #  def generate_subsequences(s, start, current):
        #         if start == len(s):
        #         result.append(current)
        #         return

        #     # Include the current character in the subsequence
        #     generate_subsequences(s, start + 1, current + s[start])

        #     # Exclude the current character from the subsequence
        #     generate_subsequences(s, start + 1, current)

        # result = []
        # generate_subsequences(text1, 0, '')
        # c1 = set(result)

        # result = []
        # generate_subsequences(text2, 0, '')
        # c2 = set(result)

        # common_subsequences = c1.intersection(c2)

        # if not common_subsequences:
        #     return 0

        # max_length = max(len(subsequence) for subsequence in common_subsequences)
        # return max_length

        # Solution 3 (Experiment)

#         def generate_combinations(s):
           
#             result = []

#             def backtrack(start, current):
#                 # Add the current combination to the result
#                 result.append(current)

#                 for i in range(start, len(s)):
#                     # Recursively generate combinations for the remaining characters
#                     backtrack(i, current + s[i])

#             # Start the recursive backtracking from index 0
#             backtrack(0, '')

#             return result

#         c1 = generate_combinations(text1)
#         c2 = generate_combinations(text2)

#         ans = 0
#         print(c1)
#         print(c2)
        
#         for x in c1:
#             if x in c2:
#                 ans = max(ans, len(x))
#                 print(x)

#         return ans

# t1 = "ezupkr"
# t2 = "ubmrapg"

# print(Solution().longestCommonSubsequence(t1, t2))

        # # Solution 2 (based on sol 1)

        # ans = 0
        # count = 0
        
        # bigger = text1 if len(text1) > len(text2) else text2
        # smaller = text2 if len(text2) < len(text1) else text1
        # print(bigger, smaller)

        # for i in range(len(smaller)):
        #     for j in range(len(bigger)):
        #         if smaller[i] == bigger[j]:
        #             print(bigger[j], smaller[i])
        #             count += 1        
        #             bigger = bigger[j+1:] 
        #             print(bigger)                    
        #             break          
                
        #     ans = max(ans, count)
            

        # return count

        # # Solution 1 brute force (edge cases need work)
        
        # ans = 0
        # count = 0
        
        # bigger = text1 if len(text1) > len(text2) else text2
        # smaller = text2 if len(text2) < len(text1) else text1
        # print(bigger, smaller)

        # for i in range(len(smaller)):
        #     for j in range(len(bigger)):
        #         if smaller[i] == bigger[j]:
        #             count += 1         
        #             break          
                
        #     ans = max(ans, count)
            

        # return count