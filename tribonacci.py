class Solution:
    def tribonacci(self, n: int) -> int:

        # Solution 1
        
        # tribList = [0, 1, 1]

        # if n < 3:
        #     match n:
        #         case 0:
        #             return tribList[0]
        #         case 1:
        #             return tribList[1]
        #         case 2:
        #             return tribList[2]

        # for i in range(2, n):
        #     tribList.append(tribList[i] + tribList[i-1] + tribList[i-2])

        # return tribList[n]

        # Solution 2

        t0 = 0
        t1 = 1
        t2 = 1

        if n < 3:
            match n:
                case 0:
                    return t0
                case 1:
                    return t1
                case 2:
                    return t2
                
        for i in range(2, n):
            temp0, temp1, temp2 = t0, t1, t2

            t2 = t0 + t1 + t2
            t0, t1 = temp1, temp2

        return t2
    
n = 4
print(Solution().tribonacci(n))
n = 33
print(Solution().tribonacci(n))