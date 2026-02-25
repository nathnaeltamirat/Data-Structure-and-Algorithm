# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def traverse(root,max_value,min_value):
            nonlocal res
            res = max(res,(max_value - min_value))
            if root.left:
                traverse(root.left,max(max_value,root.left.val),min(min_value,root.left.val))
            if root.right:
                traverse(root.right,max(max_value,root.right.val),min(min_value,root.right.val))
        traverse(root,root.val,root.val)
        return res