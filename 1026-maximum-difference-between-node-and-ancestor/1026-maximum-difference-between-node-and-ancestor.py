# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(root,curr_min,curr_max):
            nonlocal res
            if root:
                curr_min = min(curr_min,root.val)
                curr_max = max(curr_max,root.val)
                res = max(res,abs(curr_min-curr_max))
                traverse(root.left,curr_min,curr_max)
                traverse(root.right,curr_min,curr_max)
        traverse(root,root.val,root.val)
        return res