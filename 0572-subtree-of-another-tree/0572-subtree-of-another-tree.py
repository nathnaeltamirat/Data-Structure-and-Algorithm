# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSimilar(root,sRoot):
            if not sRoot and root:
                return False
            if not root and sRoot:
                return False
            if not root and not sRoot:
                return True
            if root.val != sRoot.val:
                return False
            return isSimilar(root.left,sRoot.left) and isSimilar(root.right,sRoot.right)
        def traverse(root):
            if not root:
                return False
            val = isSimilar(root,subRoot)
            return traverse(root.left) or traverse(root.right) or val
        return traverse(root)