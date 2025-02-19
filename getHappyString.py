class Solution:
    def getHappyString(self, n: int, k: int) -> str:

    # Solution 2

        happy_strings = []
        
        def backtrack(curr):
            if len(curr) == n:
                happy_strings.append(curr)
                return
            
            for ch in "abc":
                if not curr or curr[-1] != ch:  # Ensure no two adjacent chars are the same
                    backtrack(curr + ch)
                    if len(happy_strings) == k:  # Stop early if we found the k-th string
                        return
        
        backtrack("")
        
        return happy_strings[k - 1] if len(happy_strings) >= k else ""

  # Solution 1

        def generate_happy_strings(n):
            def is_happy(string):
                return all(string[i] != string[i + 1] for i in range(len(string) - 1))
            
            all_strings = (''.join(s) for s in product('abc', repeat=n))
            happy_strings = sorted(filter(is_happy, all_strings))
            
            return happy_strings

        ans = generate_happy_strings(n)

        return ans[k-1] if len(ans) >= k else ""
