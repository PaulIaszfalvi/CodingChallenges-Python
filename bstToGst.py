# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_inorder(node, sum):
            nonlocal total_sum
            if node is None:
                return
            
            reverse_inorder(node.right, sum)
            
            node_val = node.val
            node.val += total_sum
            total_sum += node_val
            
            reverse_inorder(node.left, sum)
        
        total_sum = 0
        reverse_inorder(root, total_sum)
        return root
