class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def sub(lst):

            if not lst:
                return [[]]
      
            subsets = sub(lst[1:])
            
            return subsets + [[lst[0]] + subset for subset in subsets]

        return sub(nums)
