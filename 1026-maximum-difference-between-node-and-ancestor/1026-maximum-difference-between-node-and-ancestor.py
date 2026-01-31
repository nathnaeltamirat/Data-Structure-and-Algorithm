# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def returnNodeMaximum(root,val):
            if not root:
                return 0
            dist = abs(root.val - val)
            left = returnNodeMaximum(root.left,val)
            right = returnNodeMaximum(root.right,val)
            max_dist = max(left,right)
            return max(max_dist,dist)
        def findMaximum(root):
            nonlocal res
            if not root:
                return 0
            res = max(res,returnNodeMaximum(root,root.val))
            left = findMaximum(root.left)
            right = findMaximum(root.right)
            res_max = max(left,right)
            return max(res_max,res)
        return findMaximum(root)

        # [8] max = 8  min = 8
        # [3,10]  max = 10 min = 3
        # [1 6 14] max = 14 min = 1
        # [4 7 13] 
        #he maimum and minimum should be at different level