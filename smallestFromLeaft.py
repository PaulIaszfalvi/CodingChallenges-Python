class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        # Solution 2
        
        ans = []

        def get(root, s):           
            if not root:
                return

            s += chr(root.val + ord('a'))  # Convert node value to character

            if not root.left and not root.right:
                ans.append(s[::-1])  # Append the reversed string to ans when reaching a leaf node
                return

            get(root.left, s)  # Traverse left subtree
            get(root.right, s)  # Traverse right subtree

        get(root, '')  # Start traversal from root with an empty string

        if not ans:  # If ans is empty, return an empty string
            return ''

        return min(ans)  # Return the lexicographically smallest string from ans
    

        # SOlution 1

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        ans = []
        s = ''

        def get(root, s):           

            if not root:
                return

            s += chr(root.val + ord('a'))

            if not root.left and not root.right:
                ans.append(s[::-1])

            get(root.left, s)
            get(root.right, s)

           

        get(root, s)

        return min(ans)
