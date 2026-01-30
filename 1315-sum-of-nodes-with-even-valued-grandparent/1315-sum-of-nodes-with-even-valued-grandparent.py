# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        level = [False] * 10 ** 4
        curr =  0
        res = [0]
        def traverse(root,idx):
            nonlocal res
            if root:
                if root.val % 2 == 0:
                    level[idx] = True
                else:
                    level[idx] = False
                g_idx = idx - 2
                if g_idx >= 0 and level[g_idx] == True:
                    res[0] += root.val
                traverse(root.left,idx+1)
                traverse(root.right,idx+1)

        traverse(root,0)
        return res[0]