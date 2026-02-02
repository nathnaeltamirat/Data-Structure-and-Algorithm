class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color =  [-1] *  len(graph)

        def dfs(node):
            temp = True
            for neigh in graph[node]:
                if color[neigh] == -1:
                    if color[node] == 1:
                        color[neigh] = 0
                    else:
                        color[neigh] = 1
                    temp = temp and dfs(neigh)
                elif color[node] == color[neigh]:
                    temp = False
            return temp

        result = True
        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 1
                result = result and dfs(node)
        return result