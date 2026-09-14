class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        items = set()
        visited = set()
        graph = defaultdict(list)
        for i in range(len(values)):
            val = values[i]
            a, b =  equations[i]
            items.add(a)
            items.add(b)
            graph[a].append((b,val))
            graph[b].append((a,1/val))

        def dfs(start,dest):
            res = 1
            if start == dest:
                return res
            for neigh,val in graph[start]:
                if neigh not in visited:
                    visited.add(neigh)
                    value = dfs(neigh,dest)
                   
                    if value:
                        return res * val * value
            return 0
        res = []
        for start, dest in queries:
            visited = set()
            if start not in items or dest not in items:
                res.append(-1)
            else:
                val = dfs(start,dest)
                if val:
                    res.append(val)
                else:
                    res.append(-1)
        return res
