# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        temp = []

        def traverse(root):
            if root:
                traverse(root.left)
                temp.append(root.val)
                traverse(root.right)
        traverse(root)
        return sorted(temp) == temp and len(temp) == len(set(temp))