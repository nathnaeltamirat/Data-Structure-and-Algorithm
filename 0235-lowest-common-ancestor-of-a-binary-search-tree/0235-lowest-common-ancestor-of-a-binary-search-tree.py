# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = {root:None}
        def traverse(root):
            if root:
                if root.left:
                    path[root.left] = root
                    traverse(root.left)
                   
                if root.right:
                    path[root.right] = root
                    traverse(root.right)
                    
        traverse(root)
        ancesstors = set()
        while p:
            ancesstors.add(p)
            p = path[p]
        print(ancesstors)
        while q:
            print(q)
            if q in ancesstors:
                return q
            q = path[q]