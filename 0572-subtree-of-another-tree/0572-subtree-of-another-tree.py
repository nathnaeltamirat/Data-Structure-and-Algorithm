# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checker(c_root,s_root):
            if not c_root and not s_root:
                return True
            if not c_root or not s_root:
                return False

            if c_root.val != s_root.val:
                return False
            return checker(c_root.left,s_root.left) and checker(c_root.right,s_root.right)
        res = False
        def dfs(root,subRoot):
            nonlocal res
            if root:
                res = res or checker(root,subRoot)
                dfs(root.left,subRoot)
                dfs(root.right,subRoot)
        dfs(root,subRoot)
        return res