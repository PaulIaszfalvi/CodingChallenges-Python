class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        # Solution 4
        
        xor_result = 0

        # If nums2 has an odd length, every element in nums1 affects the result
        if len(nums2) % 2 == 1:
            for num in nums1:
                xor_result ^= num

        # If nums1 has an odd length, every element in nums2 affects the result
        if len(nums1) % 2 == 1:
            for num in nums2:
                xor_result ^= num

        return xor_result


      # Solution 3

        xor1 = reduce(lambda x, y: x ^ y, nums1, 0)
        xor2 = reduce(lambda x, y: x ^ y, nums2, 0)

        return (xor1 if len(nums2) % 2 else 0) ^ (xor2 if len(nums1) % 2 else 0)

        # Solution 2

        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = []
        
        for n in nums1:
            for m in nums2:
                nums3.append(n^m)

        return reduce(lambda x, y: x ^ y, nums3)
        

      # Solution 1

        nums3 = []
        
        for n in nums1:
            for m in nums2:
                nums3.append(n^m)

        return reduce(lambda x, y: x ^ y, nums3)
        
