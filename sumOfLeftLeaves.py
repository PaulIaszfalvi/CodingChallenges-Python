# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        # Solution 2
           
        s = 0

        def get(root, is_left):
            nonlocal s
            if not root:
                return
            if not root.left and not root.right:
                if is_left:  # Only add the value if it's a left leaf
                    s += root.val
            get(root.left, True)  # Check left child as a left child
            get(root.right, False)  # Check right child as a right child

        get(root, False)  # Start traversal from the root with the indication that it's not a left child
        return s


        # Solution 1
        
        s = 0

        def get(root):

            nonlocal s           

            if not root:
                return

            if root.left:
                s += root.left.val
                get(root.left)
            
            if root.right:
                get(root.right)
           
        get(root)
        
        return s