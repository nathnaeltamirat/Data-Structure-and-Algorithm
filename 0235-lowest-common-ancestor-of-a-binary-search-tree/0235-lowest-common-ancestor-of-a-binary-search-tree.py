# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        all_path = {root:None}
        def traverse(root):
            if root:
                if root.left:
                    all_path[root.left] = root
                    traverse(root.left)
                if root.right:

                    all_path[root.right] = root
                    traverse(root.right)
        traverse(root)
        anscestor = set()

        while p:
            anscestor.add(p)
            p = all_path[p]
        while q:
            if q in anscestor:
                return q
            q = all_path[q]