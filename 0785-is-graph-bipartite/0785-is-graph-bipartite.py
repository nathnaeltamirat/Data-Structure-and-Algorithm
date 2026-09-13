class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        res = True
        def dfs(i):
            nonlocal res
            for neigh in graph[i]:
                if color[neigh] == -1:
                    color[neigh] = 1 - color[i]
                    dfs(neigh)
                elif color[neigh] == color[i]:
                    res = False
                    return False
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                dfs(i)

        return res

                   

                
            

