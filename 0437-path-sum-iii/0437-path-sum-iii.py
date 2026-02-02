# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = 0
        res = 0
        def traverse(root):
            nonlocal curr_sum,res
            if root:
                curr_sum += root.val
                res += prefix_sum[curr_sum - targetSum]
                prefix_sum[curr_sum] += 1
                
                traverse(root.left)
                traverse(root.right)
                prefix_sum[curr_sum] -= 1
                curr_sum -= root.val
                
        traverse(root)
        return res