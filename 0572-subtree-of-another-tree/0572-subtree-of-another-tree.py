# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def isSubRoot(root,sRoot):
            val = True
            if not root and sRoot or (not sRoot and root):
                return False
            if not root and not sRoot:
                return True
            if root.val != sRoot.val:
                return False
            val = val and isSubRoot(root.left,sRoot.left)
            val = val and isSubRoot(root.right,sRoot.right)

            return val
        
        def traverse(root):
            nonlocal res
            if root:
                res = res or isSubRoot(root,subRoot)
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return res
        
            

        