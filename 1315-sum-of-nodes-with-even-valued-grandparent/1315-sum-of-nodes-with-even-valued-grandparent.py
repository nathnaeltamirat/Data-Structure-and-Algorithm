# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        level = [0] * 10 ** 4
        idx = [0]
        res = [0]
        visited = set([root.val])
        def traverse(root,idx):
            if not root:
                return
            if root.val % 2 == 0:
                level[idx] = 1
            else:
                level[idx] = 0
            
            if idx - 2 >= 0 and level[idx - 2] == 1:
                res[0] += root.val
            traverse(root.left,idx+1)
            traverse(root.right,idx+1)
        traverse(root,0)
        return res[0]

