class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node,visited):
            val = False
            if node == destination:
                return True
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    val = val or  dfs(neigh,visited)
            return val
        return dfs(source,set())