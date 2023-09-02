class Solution(object):
    def compress(self, chars):
       
        if len(chars) <= 1:
           return list(chars)

        # myMap = {}

        # for i in range(len(chars)-1):
        #     if chars[i] == chars[i+1]:
        #         myMap[chars[i]] = myMap.get(chars[i], 1) + 1
        #     else:
        #         myMap[chars[i]] = myMap.get(chars[i], 0) + 1

        # result = []

        # for val, i in myMap.items():
        #     result.append(str(val))
        #     result.append(str(i))
  

        # return result

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

        return result

    
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))

chars = ["a"]
print(Solution().compress(chars))