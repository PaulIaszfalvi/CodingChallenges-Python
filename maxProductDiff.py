class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:


        # Solution 2 O(n)

        s1, s2, m1, m2 =  10**4, 0, 0, 0

        for x in nums:
            if x > m1:
                m2 = m1
                m1 = x    
            elif x > m2:
                m2 = x            
            if x < s1:                
                s2 = s1
                s1 = x
            elif x < s2:
                s2 = x
       
        return m1 * m2 - s1 * s2

        # Solution 1 O(nlogn)

        # nums.sort()

        # return (nums[-1] * nums[-2] - nums[0] * nums[1])