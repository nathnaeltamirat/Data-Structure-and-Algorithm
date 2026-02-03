class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        valid_values = set()
        for i in range(len(equations)):
            val = values[i]
            a, b = equations[i]
            graph[a].append([b,val])
            graph[b].append([a,1/val])
            valid_values.add(a)
            valid_values.add(b)
        visited = set()
        res = []
        def dfs(source, destination):
            visited.add(source)
            if source == destination:
                return 1
            val = 1
            for neigh,neigh_val in graph[source]:
                if (neigh) not in visited:
                    val  = dfs(neigh,destination)
                    if val != -1:
                        return neigh_val * val
            return -1
        for src, des in queries:
            if src not in valid_values or des not in valid_values:
                res.append(-1)
            else:
                visited = set()
                res.append(dfs(src,des))
        print(graph)
        print(res)
        return res


