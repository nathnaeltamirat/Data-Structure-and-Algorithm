class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        #using visited:
        visited = [False] * len(edges)
        node_step = {}
        res = -1
        for i in range(len(edges)):
            if visited[i]:
                continue
            node = i
            step = 0
            node_step = {}
            while node != -1 and not visited[node]:
                visited[node] = True
                node_step[node] = step
                node = edges[node]
                step += 1
                if node in node_step:
                    res = max(res,step - node_step[node])
                    break
       


        return res