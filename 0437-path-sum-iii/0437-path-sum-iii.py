# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = [0]
        curr_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        def dfs(root):
            nonlocal curr_sum
            if root:
                curr_sum += root.val
                count[0] += prefix[curr_sum - targetSum]
                prefix[curr_sum] += 1
                dfs(root.left)
                dfs(root.right)
                prefix[curr_sum] -= 1
                curr_sum -= root.val
        dfs(root)
        return count[0]
                
                