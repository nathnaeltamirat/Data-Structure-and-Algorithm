# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root,level):
            if not root:
                return root,level
            l_root, l_level = dfs(root.left,level+1)
            r_root, r_level = dfs(root.right,level+1)
            if l_level > r_level:
                return l_root, l_level
            if r_level > l_level:
                return r_root, r_level
            return root, r_level
        return dfs(root,0)[0]