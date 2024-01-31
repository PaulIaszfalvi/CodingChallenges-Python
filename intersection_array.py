class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Solution 2

        n1 = set(nums1)
        n2 = set(nums2)
        
        return n1 & n2

        # Solution 1
        
        n1 = set(nums1)
        n2 = set(nums2)

        ans = []

        for x in n1:
            if x in n2:
                ans.append(x)
                
        return ans