# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # Solution 1
        
        def get(root):

            if not root:
                return []

            ans = []
            
            ans.extend(get(root.left))
            ans.extend(get(root.right))

            if not root.left and not root.right:
                ans.append(root.val)
            
            return ans

        return get(root1) == get(root2)