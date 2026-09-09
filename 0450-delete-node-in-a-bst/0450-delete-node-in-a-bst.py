# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inorderSuccessor(root):
            while root.left:
                root = root.left
            return root
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = inorderSuccessor(root.right)
            root.val = node.val
            root.right = self.deleteNode(root.right,node.val)
        
        return root
        