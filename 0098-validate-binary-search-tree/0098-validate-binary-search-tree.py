# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def vaildChecker(root,low,high):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            
            return vaildChecker(root.left, low, root.val) and vaildChecker(root.right,root.val,high)
        return vaildChecker(root,float('-inf'),float('inf'))