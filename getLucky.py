class Solution:
    def getLucky(self, s: str, k: int) -> int:

      # Solution 2

        # Convert the string to its respective numerical representation
        n = ''.join(str(ord(char) - ord('a') + 1) for char in s)

        # Perform digit summation k times
        while k > 0:
            ans = sum(int(x) for x in n)
            n = str(ans)
            k -= 1
        
        return ans


      # Solution 1

        n = ''
        
        for char in s:
            n += str(ord(char) - ord('a') + 1)

        while k > 0:     

            ans = 0

            for x in n:
                ans += int(x)
                
            n = str(ans)
            k -= 1
            

        return ans
                
            
