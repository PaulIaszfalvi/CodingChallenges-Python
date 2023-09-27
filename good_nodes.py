# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ

class Solution:
    def goodNodes(self, root) -> int:
        def get_good_nodes(node, max_value):
            if not node:
                return 0

            # Count the current node if it's greater than or equal to max_value.
            count = 1 if node.val >= max_value else 0

            # Update max_value to the maximum between the current node's value and max_value.
            new_max_value = max(max_value, node.val)

            # Recursively count good nodes in the left and right subtrees.
            get_good_nodes(node.left, new_max_value)
            get_good_nodes(node.right, new_max_value)

            return count

        # Handle the case where the tree is empty.
        if not root:
            return 0

        # Start with the root node, and the initial max_value is the root's value.
        return get_good_nodes(root, root.val)
     
root = [3,1,4,3,None,1,5]
print(Solution().goodNodes(root))