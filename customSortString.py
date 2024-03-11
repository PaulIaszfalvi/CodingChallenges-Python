class Solution:
    def customSortString(self, order: str, s: str) -> str:

        # Alternate 

        # Count the occurrences of each character in s
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Construct the sorted string based on the order
        sorted_str = ''
        for char in order:
            if char in count:
                sorted_str += char * count[char]
                del count[char]  # Remove the character from the count

        # Append remaining characters not in order
        for char, freq in count.items():
            sorted_str += char * freq

        return sorted_str


        # Solution 1
       
        d = {}
        ans = ''
        
        for x in s:
           d[x] = d.get(x, 0) + 1

        for x in order:
            if x in d:
                ans += '' + x * d.get(x)
                del d[x]
                s = s.replace(x, '')
                    
        return ans + s