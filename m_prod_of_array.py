from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answers = []     
        bkwd = []
        product = 1

        for e in nums: 
            answers.append(product)
            product *= e
            

        product = 1

        for e in nums[::-1]:
            bkwd.append(product)
            product *= e

        bkwd.reverse()   

        for i in range(len(answers)):
            answers[i] = answers[i] * bkwd[i]
        
        return answers


        #Second Solution

        # answers = []

        # fwd = []
        # bkwd = []
        # product = 1

        # for e in nums: 
        #     fwd.append(product)
        #     product *= e
            

        # product = 1

        # for e in nums[::-1]:
        #     bkwd.append(product)
        #     product *= e

        # bkwd.reverse()   

        # for i in range(len(fwd)):
        #     answers.append(fwd[i] * bkwd[i])
        
        # return answers


        #First solution

        # answers = []
        # non_zero = []
        # zeroes = 0
        # total = total_no_zero = 1
                       
        # for e in nums:      
            
        #     total *= e
            
        #     if e is 0:
        #         zeroes += 1
        #     else:
        #         non_zero.append(e)
        #         total_no_zero *= e
            
        # for e in nums:
        #     if e is not 0:
        #         answers.append(int(total/e))
        #     else: 
        #         if zeroes > 1:
        #             answers.append(0)
        #         else:
        #             answers.append(total_no_zero)
        
        # return answers
            
nums = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(nums))  #Output: [24,12,8,6]