# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        # Solution 3

        # Function to perform inorder traversal and return the nodes in sorted order
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)
        
        # Function to build a balanced BST from sorted nodes
        def build_balanced_bst(nodes):
            if not nodes:
                return None
            mid = len(nodes) // 2
            root = nodes[mid]
            root.left = build_balanced_bst(nodes[:mid])
            root.right = build_balanced_bst(nodes[mid + 1:])
            return root
        
        # Step 1: Perform inorder traversal to get sorted nodes
        sorted_nodes = inorder(root)
        
        # Step 2: Build a balanced BST from sorted nodes
        balanced_root = build_balanced_bst(sorted_nodes)
        
        return balanced_root


        # Solution 2

        arr=[]
        def inorder(root):
            if root==None: return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        def BST(l, r):
            if l>r: return None
            m=(l+r)//2
            left=BST(l, m-1)
            right=BST(m+1, r)
            return TreeNode(arr[m], left, right)
        
        inorder(root)
        return BST(0, len(arr)-1)

        # Solution 1

        # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        
        n = math.ceil(len(arr)/2)

        def build_tree(nums, arr, n):
            if not nums:
                return None
            
            # Create a TreeNode for each element in nums
            nodes = [TreeNode(val) if val is not None else None for val in nums]
            
            # Set nodes[0] to arr[n] and remove arr[n] if n is within bounds
            if 0 <= n < len(arr):
                nodes[0].val = arr.pop(n)
            
            # Link parent nodes with their children
            for i in range(len(nodes)):
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                
                if left_index < len(nodes):
                    nodes[i].left = nodes[left_index]
                if right_index < len(nodes):
                    nodes[i].right = nodes[right_index]
            
            # Return the root of the binary tree
            return nodes[0]

        return build_tree(root, arr, n)

        
