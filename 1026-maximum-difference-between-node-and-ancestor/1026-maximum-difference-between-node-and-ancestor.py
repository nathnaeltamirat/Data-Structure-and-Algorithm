# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(min_value,root,max_value):
            nonlocal res
            if root:
                if root.val > max_value:
                    max_value = root.val
                if root.val < min_value:
                    min_value = root.val
                res = max(res,max_value - min_value)
                traverse(min_value, root.left,max_value)
                traverse(min_value,root.right,max_value)
        traverse(root.val,root,root.val)
        return res