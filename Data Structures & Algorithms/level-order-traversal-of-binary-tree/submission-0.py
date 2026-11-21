# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []
        def populate(node: Optional[TreeNode], height: int = 0):
            if not node:
                return

            if len(self.levels) <= height:
                self.levels.append([])

            self.levels[height].append(node.val)

            populate(node.left, height + 1)
            populate(node.right, height + 1)
        
        populate(root)
        
        return self.levels
            