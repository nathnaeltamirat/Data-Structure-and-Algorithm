class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        all_elements = set()
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            graph[a].append([b,value])
            graph[b].append([a,1/value])
            all_elements.add(a)
            all_elements.add(b)
        res = []
        def dfs(source,target):
            visited.add(source)
            if source == target:
                return 1
            for neigh,c_val in graph[source]:
                if neigh not in visited:
                    val = dfs(neigh,target)
                    if val != -1:
                        return val * c_val
            return -1
        visited = set()
        for a, b in queries:
            if a not in all_elements or b not in all_elements:
                res.append(-1)
            else:
                visited = set()
                val = dfs(a,b)
                if val:
                    res.append(val)
                else:
                    res.append(-1)
        return res