class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Check if it's even possible to satisfy the requirement
        freq = {'a': 0, 'b': 0, 'c': 0}
        for char in s:
            freq[char] += 1
        if freq['a'] < k or freq['b'] < k or freq['c'] < k:
            return -1
        
        # Sliding window to minimize the substring that satisfies the condition
        n = len(s)
        total = {'a': freq['a'], 'b': freq['b'], 'c': freq['c']}
        l, max_len = 0, 0
        
        for r in range(n):
            total[s[r]] -= 1
            while total['a'] < k or total['b'] < k or total['c'] < k:
                total[s[l]] += 1
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return n - max_len
