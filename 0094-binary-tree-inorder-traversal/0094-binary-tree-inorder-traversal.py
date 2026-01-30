# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverseInorder(root):
            if root:
                traverseInorder(root.left)
                res.append(root.val)
                traverseInorder(root.right)
        traverseInorder(root)
        return res