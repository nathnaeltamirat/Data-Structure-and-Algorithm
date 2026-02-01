class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        ans = [-1] * n
        result = True
        def dfs(node):
            temp = True
            for neighbour in graph[node]:
                if ans[neighbour] == -1:
                    if ans[node] == 0:
                        ans[neighbour] = 1
                    else:
                        ans[neighbour] = 0
                    temp = temp and dfs(neighbour)
                elif ans[neighbour] == ans[node]:
                    return False
            return temp
        for node in range(n):
            if ans[node] == -1:
                ans[node] = 0
                result = result and dfs(node)
        return result
            