# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(root,h,l):
            nonlocal res
            if root:
                h = max(h,root.val)
                l = min(l,root.val)
                res = max(res,h-l)
                traverse(root.left,h,l)
                traverse(root.right,h,l)
        traverse(root,float('-inf'),float('inf'))
        return res