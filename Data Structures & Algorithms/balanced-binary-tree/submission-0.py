# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.height(root)
        return self.is_balanced

    def height(self, node):
        if not node:
            return 0

        h_left = self.height(node.left)
        h_right = self.height(node.right)

        if abs(h_left - h_right) > 1:
            self.is_balanced = False

        return 1 + max(h_left, h_right)
