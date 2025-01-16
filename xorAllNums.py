class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

      # Solution 2

        xor1 = reduce(lambda x, y: x ^ y, nums1, 0)
        xor2 = reduce(lambda x, y: x ^ y, nums2, 0)

        return (xor1 if len(nums2) % 2 else 0) ^ (xor2 if len(nums1) % 2 else 0)

      # Solution 1

        nums3 = []
        
        for n in nums1:
            for m in nums2:
                nums3.append(n^m)

        return reduce(lambda x, y: x ^ y, nums3)
        
