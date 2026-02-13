# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp = []
        curr = 1
        def traverse(root):
            nonlocal curr
            if root:
                left =  traverse(root.left)
                if left != None:
                    return left 
                if curr == k:
                    return root.val
                curr += 1
                right = traverse(root.right)
                if right != None:
                    return right

            return None
        return traverse(root)
        return temp[k-1]