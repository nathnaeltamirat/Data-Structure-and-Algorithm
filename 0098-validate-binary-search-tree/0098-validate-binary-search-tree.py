# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        preorder = []
       
        def inorderT(root):
            if root:
                inorderT(root.left)
                inorder.append(root.val)
                
                inorderT(root.right)
        
        def preorderT(root):
            if root:
                preorder.append(root.val)
                preorderT(root.left)
                preorderT(root.right)

        inorderT(root)
        preorderT(root)
        if len(inorder) != len(set(inorder)):
            return False
        i = j = 0
        print(inorder,preorder)
        while i < len(inorder) and j < len(preorder):
            parent = preorder[j]
            mid = inorder.index(parent)
            for k in range(i,mid):
                if inorder[k] >= parent:
                    return False
            j += 1
        return True