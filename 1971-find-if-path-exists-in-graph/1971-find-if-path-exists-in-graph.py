class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(vertex,visited):
            if vertex == destination:
                return True
            visited.add(vertex)
            for neigh in graph[vertex]:
                if neigh not in visited:
                    if dfs(neigh,visited):
                        return True
            return False
        return dfs(source, set())
           
                    