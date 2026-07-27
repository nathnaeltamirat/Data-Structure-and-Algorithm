# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        def dfs(root):
            if root:
                dfs(root.left)
                ans.append(root)
                dfs(root.right)
        dfs(root)
        sorted_val = sorted(node.val for node in ans)
        print(sorted_val)
        for i in range(len(ans)):
            ans[i].val = sorted_val[i]
        
        