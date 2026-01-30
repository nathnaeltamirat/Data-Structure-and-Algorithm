# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def minValue(root):
            while root.left:
                root = root.left
            return root
        
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:#equal
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            temp  = minValue(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right,temp.val)
            
        return root



            

        
