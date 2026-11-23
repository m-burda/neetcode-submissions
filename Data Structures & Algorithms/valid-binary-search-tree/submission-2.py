# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lowest: int, highest: int, node: Optional[TreeNode]):
            if node is None:
                return True
            
            if node.val <= lowest or node.val >= highest:
                return False
            
            return dfs(lowest, node.val, node.left) and dfs(node.val, highest, node.right)

        return dfs(float("-inf"), float("inf"), root)
        
