# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSimilar(root,sR):
            if not root and not sR:
                return True
            if (root and not sR) or  (not root and sR):
                return False
            ans = True
            ans = ans and isSimilar(root.left,sR.left)
            if root.val != sR.val:
                return False
            ans = ans and isSimilar(root.right,sR.right)
            return ans

        def traverse(root):
            temp = False
            if root:
                temp = temp or traverse(root.left)
                if isSimilar(root,subRoot):
                    return True
                temp = temp or traverse(root.right)
            return temp
        return traverse(root,)