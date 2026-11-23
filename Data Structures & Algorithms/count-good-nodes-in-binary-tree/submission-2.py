# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def check_node(node, prev_max: int):
            if not node:
                return
            
            if node.val >= prev_max:
                self.good_nodes += 1

            prev_max = max(prev_max, node.val)

            check_node(node.left, prev_max)
            check_node(node.right, prev_max)
        
        check_node(root, -200)
        return self.good_nodes

