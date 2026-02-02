class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for  j in range(len(isConnected[i])):
                if i != j and isConnected[i][j]:
                    graph[i].append(j)
        res = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                dfs(i)
        return res
