class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        def dfs(i):
            temp = True
            for neigh in graph[i]:
                if color[neigh] == -1:
                    if color[i] == 0:
                        color[neigh] = 1
                    else:
                        color[neigh] = 0
                    temp = temp and dfs(neigh)
                elif color[neigh] == color[i]:
                    return False
            return temp
        result = True
        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                result = result and dfs(i)
        return result
