class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        # Solution 1
        
        binary_set = {int(x, 2) for x in nums}
        l = len(nums)
        bin_zeroes = bin(0)[2:]

        result = bin(0)[2:]  # Initialize result without leading zeroes

        for x in range(2**l):
            if x not in binary_set:
                k = bin(x)[2:].count('1')  # Count the number of '1' bits in the binary representation of x
                result = bin(int(result, 2) | int(bin(x)[2:].zfill(l - k), 2))[2:]           
                break

        return result.zfill(l)
    
        # Online solution 

        # res = []
        # for i in range(len(nums)):
        #     if nums[i][i] == '1':
        #         res.append('0')
        #     else:
        #         res.append('1')
        # return "".join(res)