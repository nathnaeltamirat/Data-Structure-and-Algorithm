# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = []
        def dfs(root):
            if root:
                dfs(root.left)
                temp.append(root)
                dfs(root.right)
        dfs(root)
        sorted_tree = sorted(node.val for node in temp)
        for i in range(len(temp)):
            temp[i].val = sorted_tree[i]
        print(sorted_tree)