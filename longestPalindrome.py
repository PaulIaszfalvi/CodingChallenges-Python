class Solution:
    def longestPalindrome(self, s: str) -> int:

      # Best 

      counts = {}
        odd_count_added = False
        palindrome_length = 0
        
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        for count in counts.values():
            palindrome_length += count // 2 * 2
            if count % 2 == 1:
                odd_count_added = True
        
        if odd_count_added:
            palindrome_length += 1
        
        return palindrome_length

      # Solution 2

      d = {x: s.count(x) for x in set(s)}  
        
        count = 0
        added = False

        for val in d.values():
            count += val // 2 * 2 
            if val % 2 == 1 and not added:
                added = True  
                count += 1  
        
        return count

      # Solution 1
         
        d = {x: s.count(x) for x in s}

        count = 0
        added = True

        for key, val in d.items():
            print(key, val, count)
            if val > 1:
                count += val - (val % 2)
            if added:
                if val % 2 == 1:
                    added = False
                    count += 1
        
        return count
          
