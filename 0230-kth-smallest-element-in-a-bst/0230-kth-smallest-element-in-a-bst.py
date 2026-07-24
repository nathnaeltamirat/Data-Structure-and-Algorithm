# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def traverse(root):
            nonlocal count
            if root:
                val = traverse(root.left)
                if val is not None:
                    return val
                count += 1
                if count == k:
                    return root.val
                return traverse(root.right)
        return traverse(root)
