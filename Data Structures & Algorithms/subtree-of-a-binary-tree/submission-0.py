# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(q, p):
            if q is None and p is None:
                return True
            elif not q or not p:
                return False

            return q.val == p.val and isSameTree(q.left, p.left) and isSameTree(q.right, p.right)

        if root is None and subRoot is None:
            return True
        elif not root or not subRoot:
            return False
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
