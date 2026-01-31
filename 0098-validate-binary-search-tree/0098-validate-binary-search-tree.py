# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev = None
        def inorder(root):
            nonlocal prev
            if not root:
                return True
            val = inorder(root.left)
    
            if prev is not None and root.val <= prev:
                return False
            prev = root.val
            val = val and inorder(root.right)
            return val
        return inorder(root)