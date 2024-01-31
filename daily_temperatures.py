class Solution:
    def dailyTemperatures(self, temperatures):

        # Solution January 2024        
        
        ans = []        

        for i, v in enumerate(t):

            f = i + 1
            count = 0

            while f < len(t):                          

                if t[f] > v:
                    ans.append(f - i)
                    break

                f += 1
            else: 
                ans.append(0)
       

        return ans


        # Solution September 2023 
        
        stack = []
        output = [0] * len(temperatures)

        # Solution 1

        for i, v in enumerate(temperatures):  
            while stack and v > stack[-1][1]:
                temp_i, temp_v = stack.pop()
                output[temp_i] = i - temp_i
          
            stack.append([i, v])  

        return output

temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))




# Faster online solution 

# result = [0] * len(temperatures) # having list with 0`s elements of same lenght as temperature array.
#         stack = [] # taking empty stack. 
#         for index, temp in enumerate(temperatures): # Traversing through provided list. 
#             while stack and temperatures[stack[-1]] < temp: # stack should not be empty and checking previous temp with current temp. 
#                 # the above while loop and taking stack for saving index is very common practice in monotonic stack questions. Suggestion: understand it properly. 
#                 prev_temp = stack.pop() # stack.pop() will provide index of prev temp, taking in separate var as we are using it more then on place. 
#                 result[prev_temp] = index - prev_temp #at the index of prev_temp and i - prev_temp by this we`ll get how many step we moved to have greater temp. 
#             stack.append(index) # in case stack is empty we`ll push index in it. 

#         return result 