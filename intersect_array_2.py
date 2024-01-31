class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
               
        d1, d2 = {}, {}
        ans = []

        for x in nums1:
            d1[x] = d1.get(x, 0) + 1
        
        for x in nums2:
            d2[x] = d2.get(x, 0) + 1

        for x, y in d1.items():
            if x in d2:
                c = min(d2.get(x), y)
                ans.extend([x]*c)
        return ans