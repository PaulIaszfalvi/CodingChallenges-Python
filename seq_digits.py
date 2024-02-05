class Solution:
        
    def sequentialDigits(self, low: int, high: int):

        # Solution 2
        
               
        ans = []
        num = 1
        c = num + 1

        if low >= high:
            return []

        #generate starting num
        while len(str(num)) < len(str(low)):            
            num = (num) *10 + c
            c += 1
        
        final = num
        if num >= low:
            ans.append(num)

        while num <= high:
            num_str = str(num)
            last = int(num_str[-1]) + 1
            num = int(num_str[1:])
            
            if last <= 9:
                num = num * 10 + last
                if low <= num <= high:
                    ans.append(num)
               
            else:
                num = final = final * 10 + int(str(final)[-1]) + 1
                if low <= num <= high:                
                    ans.append(num)
                else:
                    break
           
        return ans

        # Solution 1 Brue force using pattern (on paper) O(n)

        # seq = [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        
        # l = 0
        # h = 0  
        # l_set = True
        
        # if low >= high:
        #     return []

        # for i, v in enumerate(seq):
        #     if v >= low and l_set:
        #         l_set = False
        #         l = i

        #     if v <= high:
        #         h = i

        # return seq[l: h+1]

low = 100
high = 300000
print(Solution().sequentialDigits(low, high))

