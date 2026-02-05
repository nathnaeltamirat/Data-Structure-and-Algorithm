class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res = -1
        n  = len(edges)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                node = i
                step = 0
                node_to_step = {}
                while node != -1:
                    if visited[node]:
                        break
                    if node in node_to_step:
                        res = max(res, step - node_to_step[node])
                        break
                    node_to_step[node] = step
                    step += 1
                    node = edges[node]
                for node in node_to_step:
                    visited[node] = True
        return res