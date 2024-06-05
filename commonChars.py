class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

      # Best

        min_freq = Counter(words[0])
        for word in words:
            min_freq &= Counter(word)
        return list(min_freq.elements())

      # Solution 2

      min_counts = {}
        
        # Initialize min_counts with counts from the first word
        for char in words[0]:
            min_counts[char] = min_counts.get(char, 0) + 1
        
        # Update min_counts with counts from the remaining words
        for word in words[1:]:
            word_counts = {}
            for char in word:
                word_counts[char] = word_counts.get(char, 0) + 1
            for char, count in min_counts.items():
                min_counts[char] = min(count, word_counts.get(char, 0))
        
        # Construct the list of common characters
        common_chars = []
        for char, count in min_counts.items():
            common_chars.extend([char] * count)
        
        return common_chars

        # Solution 1

        ans = []
        
        # Count occurrences of characters in each word
        for word in words:
            d = {x: word.count(x) for x in word}
            ans.append(d)

        # Find the minimum count for each character among all words
        res = ans[0].copy()
        for d in ans[1:]:
            for key, value in res.items():
                if key not in d:
                    res[key] = 0  # If the key is not present in the current dictionary, set count to 0
                else:
                    res[key] = min(res[key], d[key])  # Update count to the minimum value found so far

        # Create a list of common characters based on the minimum counts
        common_chars = []
        for key, value in res.items():
            common_chars.extend([key] * value)

        return common_chars
