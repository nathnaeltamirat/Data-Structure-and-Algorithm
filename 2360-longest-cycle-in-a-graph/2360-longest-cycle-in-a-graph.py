class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False] * len(edges)
        res = -1
        for i in range(len(edges)):
            if visited[i]:
                continue
            step = 0
            path_step = {}
            node = i
            while node != -1  and not visited[node]:
                visited[node] = True
                path_step[node] = step
                step += 1
                node = edges[node]
                if node in path_step:
                    res = max(res,step - path_step[node])
                    break
        return res