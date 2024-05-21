# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        # Solution 1

        def rec(root):
            if not root:class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def sub(lst):

            if not lst:
                return [[]]
      
            subsets = sub(lst[1:])
            
            return subsets + [[lst[0]] + subset for subset in subsets]

        return sub(nums)

                return None

            if root.val == 0:
                return False
            elif root.val == 1:
                return True
            elif root.val == 2:
                return rec(root.left) or rec(root.right)
            elif root.val == 3:
                return rec(root.left) and rec(root.right)

        return rec(root)
