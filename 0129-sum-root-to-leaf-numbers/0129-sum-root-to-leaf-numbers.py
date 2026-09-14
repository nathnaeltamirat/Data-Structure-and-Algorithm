# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root,path):
            if root:
                if not root.left and not root.right:
                    path.append(str(root.val))
                    res.append(int("".join(path)))
                    path.pop()
                    return
                path.append(str(root.val))
                dfs(root.left,path)
                dfs(root.right,path)
                path.pop()
        dfs(root,[])
        return sum(res)