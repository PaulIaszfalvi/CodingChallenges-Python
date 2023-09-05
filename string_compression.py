class Solution(object):
    def compress(self, chars):
 
        char = chars[0]
        result = ''
        count = 0

        for c in chars:
            if char == c:
                count += 1
            else:
                result += char + str(count)              
                count = 1
                char = c
        
        result += char + str(count)   

        return list(str(result))


chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))