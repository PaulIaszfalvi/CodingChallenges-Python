class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:


      from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
      # Solution 3
      
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        ans = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return ans


        # Solution 2
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        ans = []
                
        for num in count1:
            if num in count2:
               
                ans.extend([num] * min(count1[num], count2[num]))

      # Solution 1
        
        n1 = {x: nums1.count(x) for x in nums1}
        n2 = {x: nums2.count(x) for x in nums2}

        ans = []

        for k, v in n1.items():
            if k in n2:
                smaller = n1[k] if n1[k] < n2[k] else n2[k]
                ans.extend([k] * smaller)

        return ans
