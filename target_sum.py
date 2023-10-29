from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int):
        def isSum(node, current_sum):
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right and current_sum == targetSum:
                return True

            return isSum(node.left, current_sum) or isSum(node.right, current_sum)

        return isSum(root, 0)

# Construct the binary tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

targetSum = 22
print(Solution().hasPathSum(root, targetSum))
