# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        temp = []
        def allPath(root):
            if root:
                temp.append(str(root.val))
                allPath(root.left)
                allPath(root.right)
                if root.left == None and root.right == None:
                    res.append("->".join(temp))
                temp.pop()
        allPath(root)
        return res
                