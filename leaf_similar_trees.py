# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Solution 1
       
        # oneList, twoList = [], []

        # self.getLeafs(root1, oneList)
        # self.getLeafs(root2, twoList)

        # return oneList == twoList


        # def getLeafs(self, root, arrList):

        # if not root.left and not root.right:
        #     arrList.append(root.val)

        # if root.left:            
        #     self.getLeafs(root.left, arrList)
        # if root.right:
        #     self.getLeafs(root.right, arrList)
      

        # Solution 2

        def compareTrees(root):
            
            if not root: return[]

            if not root.left and not root.right:
                    return [root.val]
                
            return compareTrees(root.left) + compareTrees(root.right)
            
        return compareTrees(root1) == compareTrees(root2)
        

     