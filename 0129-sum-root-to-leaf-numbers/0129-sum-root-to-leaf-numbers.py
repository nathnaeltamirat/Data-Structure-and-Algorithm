# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def traverse(root,temp):
            if root:
                if not root.left and not root.right:
                    temp.append(str(root.val))
                    if temp:
                        res.append(int("".join(temp)))
                    temp.pop()
                    return 
                temp.append(str(root.val))
                traverse(root.left, temp)
                traverse(root.right,temp)
                temp.pop()
        traverse(root,[])
        return sum(res)