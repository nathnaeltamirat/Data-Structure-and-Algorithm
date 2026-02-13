# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        anecsstor = {root:None}
        def traverse(root):
            if root:
                if root.left:
                    anecsstor[root.left] = root
                    traverse(root.left)
                if root.right:
                    anecsstor[root.right] = root
                    traverse(root.right)
        traverse(root)
        p_anecsstor = set()
        p_anecsstor.add(p)
        while anecsstor[p]:
            p_anecsstor.add(anecsstor[p])
            p = anecsstor[p]
        if q in p_anecsstor:
            return q
        while anecsstor[q]:
            if anecsstor[q] in p_anecsstor:
                return anecsstor[q]
            q = anecsstor[q]
