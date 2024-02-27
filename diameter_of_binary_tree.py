class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Solution 1

        # Helper function to calculate the depth and diameter of a subtree
        def calculate_depth_and_diameter(node):
            if not node:
                return 0, 0

            # Recursively calculate the depth and diameter of the left subtree
            left_depth, left_diameter = calculate_depth_and_diameter(node.left)
            
            # Recursively calculate the depth and diameter of the right subtree
            right_depth, right_diameter = calculate_depth_and_diameter(node.right)
            
            # Calculate the depth of the current node
            depth = 1 + max(left_depth, right_depth)
            
            # Calculate the diameter passing through the current node
            diameter_through_node = left_depth + right_depth
            
            # Return the depth and the maximum diameter among left, right, and through-node diameters
            return depth, max(left_diameter, right_diameter, diameter_through_node)

        # Start the calculation from the root node
        _, diameter = calculate_depth_and_diameter(root)
        
        return diameter

        # Faster online solution
    
        # Define a recursive function to calculate the diameter
        def diameter(node, res):
            # Base case: if the node is None, return 0
            if not node:
                return 0
            
            # Recursively calculate the diameter of left and right subtrees
            left = diameter(node.left, res)
            right = diameter(node.right, res)

            # Update the maximum diameter encountered so far
            res[0] = max(res[0], left + right)
            
            # Return the depth of the current node
            return max(left, right) + 1
        
        # Initialize a list to hold the maximum diameter encountered
        res = [0]
        # Call the diameter function starting from the root
        diameter(root, res)
        # Return the maximum diameter encountered
        return res[0]