class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Solution 1

        # result1 = []
        # result2 = []

        # for e in nums1:
        #     if e not in nums2:
        #         result1.append(e)

        # for e in nums2:
        #     if e not in nums1:
        #         result2.append(e)

        # return [set(result1), set(result2)]

        # Solution 2

        # dict1 = {}
        # dict2 = {}

        # for e in nums1:
        #     dict1[e] = dict1.get(e, 0) + 1

        # for e in nums2:
        #     dict2[e] = dict2.get(e, 0) + 1

        # result1 = {k:v for k,v in dict1.items() if k not in dict2}
        # result2 = {k:v for k,v in dict2.items() if k not in dict1}

        # return [list(result1), list(result2)]


        # Solution 3

        return [list(set(nums1)-set(nums2)), list(set(nums2)-set(nums1))]


nums1 = [1,2,3]
nums2 = [2,4,6]

print(Solution().findDifference(nums1, nums2))

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

print(Solution().findDifference(nums1, nums2))