# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr_sum = 0
        res = 0
        def traverse(root):
            nonlocal res, curr_sum
            if root:
                curr_sum += root.val
               

                res += prefix[curr_sum - targetSum]
                prefix[curr_sum] += 1
                traverse(root.left)
                traverse(root.right)
                prefix[curr_sum]-=1
                curr_sum -= root.val
        traverse(root)
        return res