# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        # Solution 2 (fails some cases)

        def getH(r, s):
    
            if not r:
                return 0

            if r.val == s and not r.left and not r.right:
                return 0  # For the case of one node

            left_height = getH(r.left, s)
            right_height = getH(r.right, s)

            height = max(left_height, right_height) + 1

            if r.val == s:
                return height

            return height

        return getH(root, start)


        # Solution 1 (fails some cases)

        def getH(r, s):
    
            if not r:
                return 0

            if r.val == s:
                return 0  # For the case of one node

            left_height = getH(r.left, s)
            right_height = getH(r.right, s)

            height = max(left_height, right_height) + 1

            if r.val == s:
                return height

            return height

        return getH(root, start)

        # Solution 1 (Rough)
        
        # def getH(r, s):

        #     if not r:
        #         return 0

        #     height = 0

        #     getH(r.left, s)
        #     getH(r.right, s)

        #     height += 1

        #     if r.val == s:
        #         return height

        #     return height

        # return getH(root, start) 
        

        # Online Solution (works 100%)
    
        def dfs(node):
                if node is None:
                    return
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                dfs(node.left)
                dfs(node.right)

            graph = defaultdict(list)
            dfs(root)
            visited = set()
            queue = deque([start])
            time = -1
            while queue:
                time += 1
                for _ in range(len(queue)):
                    current_node = queue.popleft()
                    visited.add(current_node)
                    for neighbor in graph[current_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            return time
    