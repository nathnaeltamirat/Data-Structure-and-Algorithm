# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        res = []
        def traverse(root):
            if root:
                stack.append(str(root.val))
                if not root.left and not root.right:
                    res.append(int("".join(stack)))
                    stack.pop()
                else:
                    traverse(root.left)
                    traverse(root.right)
                    stack.pop()
        traverse(root)
        print(res)
        return sum(res)