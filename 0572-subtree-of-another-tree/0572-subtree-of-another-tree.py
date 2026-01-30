# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = [False]
        def isSimilar(root,subRoot):
            if not root and not subRoot:
                return True
            if (root and not subRoot) or (subRoot and not root) or (not root.left and subRoot.left ) or(not root.right and  subRoot.right):
                return False
            if root.val != subRoot.val:
                return False
            val = True
            if root.left:
                val = val & isSimilar(root.left,subRoot.left)
            if root.right:
                val = val & isSimilar(root.right,subRoot.right)
            
            return val

        def solver(root):
            if root:
                if isSimilar(root,subRoot):
                    res[0] = True
                    return
                solver(root.left)
                solver(root.right)
            
        solver(root)
        return res[0]