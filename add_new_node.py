# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def insert(root, d):
            if not root:
                return
            if d == depth - 1:               
                left_node = TreeNode(val)
                right_node = TreeNode(val)
                left_node.left = root.left
                right_node.right = root.right
                root.left = left_node
                root.right = right_node
            else:
                insert(root.left, d + 1)
                insert(root.right, d + 1)
                
        # Special case for adding at depth 1
        if depth == 1:           
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        insert(root, 1)
        return root