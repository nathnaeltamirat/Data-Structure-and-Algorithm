# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidChecker(low,root,high):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return isValidChecker(low,root.left,root.val) and isValidChecker(root.val,root.right,high)
        return isValidChecker(float('-inf'),root,float('inf'))