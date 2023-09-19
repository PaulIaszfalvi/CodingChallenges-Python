# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Solution 1

        # result = []

        # def getRight(root):

           
        #     if not root:
        #         return []
        #     else:
        #         if root.right:
        #             return result + [root.val] + getRight(root.right)
        #         else:
        #             return result + [root.val]

        # return getRight(root)

        # Solution 2

        def solve(root, lvl):
            if root:
                if len(res)==lvl:
                    res.append(root.val)
                solve(root.right, lvl + 1)
                solve(root.left, lvl + 1)
            return 

        res = []
        solve(root,0)
        return res