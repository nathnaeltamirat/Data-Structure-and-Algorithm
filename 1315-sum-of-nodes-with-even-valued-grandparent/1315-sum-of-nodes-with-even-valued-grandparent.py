# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def traversal(root,parent,grandParent):
            if root:
                if grandParent is not None and grandParent % 2 == 0:
                    res[0] += root.val
                grandParent = parent
                parent = root.val
                traversal(root.left,parent,grandParent)
                traversal(root.right,parent,grandParent)
        traversal(root,None,None)
        return res[0]