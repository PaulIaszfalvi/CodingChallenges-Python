class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

      # Solution     

        # Create a set for quick look-up of dictionary words
        word_set = set(dictionary)
        n = len(s)
        
        # dp[i] will be the minimum extra characters needed for s[0:i]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Initially assume all characters up to i are extra
            dp[i] = dp[i - 1] + 1
            
            # Check for every possible word in the dictionary
            for word in word_set:
                word_len = len(word)
                # If the current substring matches a word
                if i >= word_len and s[i - word_len:i] == word:
                    # Update dp[i] if using this word gives fewer extra characters
                    dp[i] = min(dp[i], dp[i - word_len])
        
        return dp[n]


        # Rough test case (trial)
        
        set1 = set(s)
        set2 = set(''.join(dictionary))

        return len(set1 - set2)
