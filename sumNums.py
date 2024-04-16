class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, path):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans += path * 10 + node.val
                return
            dfs(node.left, path * 10 + node.val)
            dfs(node.right, path * 10 + node.val)
        
        ans = 0
        dfs(root, 0)
        return ans
    

    # Not Working for all test cases# Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    class Solution:
        def sumNumbers(self, root: Optional[TreeNode]) -> int:
            # Define the modulo value
            m = 10 ** 9 + 7
            
            # Define the recursive function to calculate the sum of root-to-leaf numbers
            def gen(root, current_sum):
                if not root:
                    return 0
                
                # Update the current sum
                current_sum = (current_sum * 10 + root.val) % m
                
                # If it's a leaf node, return the current sum
                if not root.left and not root.right:
                    return current_sum
                
                # Recursively calculate the sum for left and right subtrees
                left_sum = gen(root.left, current_sum)
                right_sum = gen(root.right, current_sum)
                
                # Return the sum of left and right subtree sums
                return (left_sum + right_sum) % m
            
            # Start the recursion from the root node with an initial sum of 0
            return gen(root, 0)

        # First draft solution

        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        class Solution:
            def sumNumbers(self, root: Optional[TreeNode]) -> int:
                
                m = 2**32

                def gen(root, level):

                    if not root:
                        return

                    level += 1

                    left = root.val + gen(root.left, level)
                    right = root.val + gen(root.right, level)

                    return left + right


                return gen(root, 0)    

                