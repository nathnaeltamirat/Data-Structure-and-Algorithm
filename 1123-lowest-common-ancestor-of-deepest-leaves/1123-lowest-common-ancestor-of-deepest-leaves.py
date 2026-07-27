# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = [root,0]
        def dfs(root,level):
            if not root:
                return  None,level
            root_l,l_val = dfs(root.left,level+1)
            root_r, r_val = dfs(root.right,level+1)
            if l_val > r_val:
                return root_l, l_val
            if r_val > l_val:
                return root_r, r_val
            return root,r_val

        return dfs(root,0)[0]
      
          
        

