# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def findMaximum(root,curr_min,curr_max):
            nonlocal res
            if not root:
                return 0
            curr_min = min(curr_min,root.val)
            curr_max = max(curr_max,root.val)
    
            left = findMaximum(root.left,curr_min,curr_max)
            right = findMaximum(root.right,curr_min,curr_max)

            return max(curr_max-curr_min,left,right)
        return findMaximum(root,root.val,root.val)

        # [8] max = 8  min = 8
        # [3,10]  max = 10 min = 3
        # [1 6 14] max = 14 min = 1
        # [4 7 13] 
        #he maimum and minimum should be at different level