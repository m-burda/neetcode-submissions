# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes_cnt = 0
        def dfs(max_val: int, node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            max_val = max(max_val, node.val)
            
            l = dfs(max_val, node.left)
            r = dfs(max_val, node.right)

            return l + r + (1 if node.val >= max_val else 0)
        
        return dfs(root.val, root)

