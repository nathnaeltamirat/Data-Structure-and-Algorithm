# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root:None}

        def dfs(root):
            if root.left:
                parent[root.left] = root
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                dfs(root.right)
        dfs(root)
        # print(parent)

        anccestor = set()
        while p:
            anccestor.add(p)
            p = parent[p]
        
        while q:
            if q in anccestor:
                return q
            q = parent[q]