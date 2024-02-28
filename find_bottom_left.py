# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # Easy online

        if not root:
            return None
        
        queue = deque([root])
        leftmost = None

        while queue:
            leftmost = queue.popleft()

            if leftmost.right:
                queue.append(leftmost.right)
            if leftmost.left:
                queue.append(leftmost.left)

        return leftmost.val

        # Solution 2

        def dfs(node, depth, leftmost):
            nonlocal max_depth, bottom_left_value
            if not node:
                return
            
            # If the current depth is greater than the maximum depth encountered so far,
            # update the maximum depth and the bottom-left value
            if depth > max_depth:
                max_depth = depth
                bottom_left_value = node.val
            
            # Recursively traverse the left and right subtrees, incrementing the depth
            dfs(node.left, depth + 1, leftmost)
            dfs(node.right, depth + 1, leftmost)
        
        max_depth = 0  # Initialize the maximum depth
        bottom_left_value = None  # Initialize the bottom-left value
        
        # Start the DFS traversal from the root node with depth 1
        dfs(root, 1, True)
        
        return bottom_left_value

        # Solution 1
        
        if not root:
            return None
        
        queue = deque([root])
        leftmost_value = None
        
        while queue:
            level_size = len(queue)
            leftmost_value = queue[0].val
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost_value

