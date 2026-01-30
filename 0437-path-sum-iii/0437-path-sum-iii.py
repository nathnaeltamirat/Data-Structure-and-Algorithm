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

        
        def solver(root,curr_sum):
            if not root:
                return 0
            
            curr_sum += root.val
            count = prefix[curr_sum - targetSum]

            prefix[curr_sum] += 1
            count += solver(root.left,curr_sum)
            count += solver(root.right,curr_sum)
            prefix[curr_sum] -= 1
            return count
        return solver(root,0)

            