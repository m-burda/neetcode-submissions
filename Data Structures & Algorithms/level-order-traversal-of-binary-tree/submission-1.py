# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
        queue = collections.deque()
        queue.appendleft(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop()

                if node.left:
                    level.append(node.left.val)
                    queue.appendleft(node.left)
                if node.right:
                    level.append(node.right.val)
                    queue.appendleft(node.right)
            if level:
                res.append(level)
        
        return res

            