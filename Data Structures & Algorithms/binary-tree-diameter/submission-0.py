# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            left = 1 + height(node.left)
            right = 1 + height(node.right)

            self.diameter = max(self.diameter, left + right)
            return max(left, right)
        
        height(root)
        
        return self.diameter