# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        q = deque([root])
        while q:
            n = len(q)
            temp = []
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    temp.append(node.right.val)
            if temp:
                res.append(temp)
        return res
