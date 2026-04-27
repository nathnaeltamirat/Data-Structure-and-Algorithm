# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]
        def traverse(root,max_value,min_value):
            res[0] = max(res[0],(max_value-min_value))
            if root.left:
                traverse(root.left,max(root.left.val,max_value),min(root.left.val,min_value))
            if root.right:
                traverse(root.right,max(root.right.val,max_value),min(root.right.val,min_value))
        traverse(root,root.val,root.val)
        return res[0]
                
