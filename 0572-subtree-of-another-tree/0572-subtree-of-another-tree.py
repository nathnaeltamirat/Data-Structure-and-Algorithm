# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checker(r,sr):
            if not r and not sr:
                return True
            if not r or not sr:
                return False
            if r.val != sr.val:
                return False
            return checker(r.left,sr.left) and checker(r.right,sr.right)
        
        val = False
        def traverse(root):
            nonlocal val
            if root:
                val = val or checker(root,subRoot)
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return val
