# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        def traverse(root):
            nonlocal count
            if root:
                val = traverse(root.left)
                if val:
                    return val
                if count == k:
                    count += 1
                    return root.val
                count += 1
                val = traverse(root.right)
                if val:
                    return val
            return 0
        return traverse(root)
        
