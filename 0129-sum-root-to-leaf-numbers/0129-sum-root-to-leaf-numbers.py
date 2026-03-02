# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def backtrack(root,path):
            nonlocal res
            if root:
                if not root.left and not root.right:
                    path.append(str(root.val))
                    val = int("".join(path))
                    res += val
                    path.pop()
                path.append(str(root.val))
                backtrack(root.left,path)
                backtrack(root.right,path)
                path.pop()
        backtrack(root,[])
        return res