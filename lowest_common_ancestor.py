class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root: TreeNode, p : TreeNode, q : TreeNode) -> TreeNode:       
        
        while root:            
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else: 
                return root



# root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4

# sol = Solution()
# print(sol.lowestCommonAncestor())