# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        # Solution 2

        def dfs(node, freq):
            if not node:
                return 0

            freq[node.val] += 1

            if not node.left and not node.right:
                # Leaf node, check if the path is a pseudo-palindrome
                odd_count = sum(count % 2 for count in freq)
                return 1 if odd_count <= 1 else 0

            # Recursive calls for left and right subtrees
            count = dfs(node.left, freq[:])  # Create a copy of freq to avoid modifying it for the left subtree
            count += dfs(node.right, freq)

            return count

        return dfs(root, [0] * 10)
        

        # Solution 1 

        def is_pseudo_palindrome(path):
            # Check if the path forms a pseudo-palindrome
            # (at most one digit can have an odd frequency)
            freq = [0] * 10
            for val in path:
                freq[val] += 1
            odd_count = 0
            for count in freq:
                if count % 2 != 0:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True
        
        def dfs(node, path):
            if not node:
                return 0
            
            path.append(node.val)
            if not node.left and not node.right:
                # Leaf node, check if the path is a pseudo-palindrome
                return 1 if is_pseudo_palindrome(path) else 0
            
            # Recursive calls for left and right subtrees
            count = dfs(node.left, path[:]) # Create a copy of freq to avoid modifying it for the left subtree
            count += dfs(node.right, path[:])
            
            return count
        
        return dfs(root, [])
    
        # More eficient online solution
    
        class Solution:
            def pseudoPalindromicPaths(self, root):
                return self.countPseudoPalindromicPaths(root, 0)

            def countPseudoPalindromicPaths(self, node, path):
                if not node:
                    return 0

                path ^= 1 << node.val

                if not node.left and not node.right:
                    return 1 if path & (path - 1) == 0 else 0

                return self.countPseudoPalindromicPaths(node.left, path) + self.countPseudoPalindromicPaths(node.right, path)

