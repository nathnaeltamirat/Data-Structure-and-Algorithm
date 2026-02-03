# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #finding high depth leafes


        def dfs(root):
            if not root:
                return [0,None]
            l_level, l_lca = dfs(root.left)
            r_level , r_lca = dfs(root.right)

            if l_level > r_level:
                return [l_level + 1, l_lca]
            if l_level < r_level:
                return [r_level + 1, r_lca]
            
            return [l_level + 1, root]
        return dfs(root)[1]





