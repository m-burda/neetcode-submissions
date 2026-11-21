# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        q = collections.deque()
        q.appendleft(root)

        while q:
            visible = None

            for _ in range(len(q)):
                node = q.pop()
                if not visible:
                    visible = node.val

                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
            
            if visible:
                res.append(visible)

        return res