# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(root,min_sum,max_sum):
            nonlocal res
            if root:
                min_sum = min(root.val,min_sum)
                max_sum = max(root.val,max_sum)

                res = max(res,max_sum - min_sum)
                traverse(root.left,min_sum,max_sum)
                traverse(root.right,min_sum,max_sum)
        traverse(root,float('inf'),float('-inf'))
        return res