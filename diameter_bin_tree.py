# define a Class Tree, to intiate the binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root):
            nonlocal diameter
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        diameter = 0
        height(root)
        return diameter
 
# Test the algorithm
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
 
print(diameterOfBinaryTree(root))