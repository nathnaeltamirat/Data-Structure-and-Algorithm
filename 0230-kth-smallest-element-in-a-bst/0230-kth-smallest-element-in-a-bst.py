# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes  = []
        heapify(nodes)
        def traverse(root):
            if not root:
                return
            heappush(nodes,root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        for i in range(k-1):
            heappop(nodes)
        return nodes[0]

