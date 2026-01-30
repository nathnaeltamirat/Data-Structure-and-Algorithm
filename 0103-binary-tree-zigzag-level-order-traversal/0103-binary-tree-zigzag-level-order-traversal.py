# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []
        q = deque([root])
        res = [[root.val]]
        while q:
            temp = []
            n = len(q)
            for _ in range(n):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                    temp.append(root.left.val)
                if root.right:
                    q.append(root.right)
                    temp.append(root.right.val)
            if temp:
                res.append(temp)
        for i in range(len(res)):
            if i % 2:
                res[i] = res[i][::-1]
        return res
