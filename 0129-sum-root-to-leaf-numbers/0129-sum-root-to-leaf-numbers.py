# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        temp = []
        def traverse(root):
            nonlocal temp,res
            if root:
                if not root.left and not root.right:
                    temp.append(str(root.val))
                    res.append(int("".join(temp)))
                    temp.pop()
                temp.append(str(root.val))
                traverse(root.left)
                traverse(root.right)
                temp.pop()
        traverse(root)
        return sum(res)