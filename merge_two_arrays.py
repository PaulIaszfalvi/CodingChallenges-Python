class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # nums3 = [x for x in nums1]

        # first = 0
        # second = 0
   
        # for i in range(m+n):

        #     if first < m:       
        #         print("i", i, "first, second", first, second)         
        #         if nums3[first] <= nums2[second]:
        #             nums1[i] = nums3[first]
        #             first += 1
        #             print(1,first, nums1[i])
                    
        #         elif second < n and nums2[second] <= nums3[first]:
        #             nums1[i] = nums2[second]
        #             second += 1
        #             print(2, nums1[i])

        #     elif second < n:
        #         print("i", i, "first, second", first, second) 
        #         nums1[i] = nums2[second]
        #         second += 1
        #         print(3, nums1[i])

            
        # print(nums1)

       
        index = m + n - 1
        a = m - 1
        b = n - 1

        while b >= 0:

            if a >= 0 and nums1[a] > nums2[b]:
                    nums1[index] = nums1[a] 
                    a -= 1
            else: 
                nums1[index] = nums2[b]
                b -= 1
           
          
            index -= 1

        print(nums1)


n1 = [1,2,3,0,0,0]
n2 = [2,5,6]
m = 3
n = 3 

Solution().merge(n1, m, n2, n)