class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        def dfs(node):
            temp = True
            for neigh in graph[node]:
                if color[neigh] == -1:
                    if color[node] == 0:
                        color[neigh] = 1
                    else:
                        color[neigh] = 0
                    temp = temp and dfs(neigh)
                elif color[neigh] == color[node]:
                    return False
            return temp


        result = True
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                print(i)
                result = result and dfs(i)
        return result