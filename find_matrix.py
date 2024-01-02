class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        # Solution 2

        n = {}
        result = []

        for x in nums:
            n[x] = n.get(x, 0) + 1

        while n:
            temp = []

            for char, count in list(n.items()):
                temp.extend([char])
                n[char] -= 1
                if n[char] == 0:
                    del n[char]

            result.append(temp)

        return result
    
        # Solution 1
    
        # n = {}
        # result = []

        # for x in nums:
        #     n[x] = n.get(x, 0) + 1

        # while len(n) > 0:
        #     temp = []

        #     for char, count in list(n.items()):
        #         temp.append(char)
        #         if count > 1:   
        #             n[char] -= 1                   
        #         else:
        #             del n[char]

        #     result.append(temp)
        
        # return result
        

        # Solution 1 prototype
        # n = {}
        # result = []

        # for x in nums:
        #     n[x] = n.get(x, 0) + 1

        # while len(n) > 0:
        #     temp = []

        #     for char, count in list(n.items()):
        #         if count > 1:
        #             if char not in temp:
        #                 n[char] -= 1
        #                 temp.append(char)
        #         else:
        #             del n[char]

        #     result.append(temp)
        
        # return result
        