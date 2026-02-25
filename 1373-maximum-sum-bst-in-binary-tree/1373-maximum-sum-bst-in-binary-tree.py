# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(root):
            nonlocal res
            if not root:
                return [True,0,float('inf'),float('-inf')]
            l_bst,l_sum,l_min,l_max = traverse(root.left)
            r_bst,r_sum, r_min,r_max = traverse(root.right)

            if l_bst and r_bst and  l_max < root.val < r_min:
                curr_sum = root.val + l_sum + r_sum
                res = max(res,curr_sum)
                return[
                    True,
                    curr_sum,
                    min(l_min,root.val),
                    max(r_max,root.val)
                ]
            return [
                False,
                0,
                float('inf'),
                float('-inf')
            ]
        traverse(root)
        return res