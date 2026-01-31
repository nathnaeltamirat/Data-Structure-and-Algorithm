# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0
        def traverse(root):
            nonlocal count,res
            if not root:
                return
            traverse(root.left)
            count += 1
            if count == k:
                res = root.val
                return
            traverse(root.right)
        traverse(root)
        return res