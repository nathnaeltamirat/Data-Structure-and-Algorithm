class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        all_items = set()
        graph = defaultdict(list)
        for i in range(len(equations)):
            equation = equations[i]
            val = values[i]
            a, b = equation
            graph[a].append([b,val])
            graph[b].append([a,1/val])
            all_items.add(a)
            all_items.add(b)
        
        visited = set()
        def dfs(node,target):
            if node == target:
                return 1
            visited.add(node)
            for neigh,next_val in graph[node]:
                if neigh not in visited:
                    
                    val =  dfs(neigh,target)
                    if val:
                        return val * next_val 
            return 0
        
        res = []
        for a, b in queries:
            if a not in all_items or b not in all_items:
                res.append(-1)
                continue
            visited = set()
            val =  dfs(a,b)
            if val:
                res.append(val)
            else:
                res.append(-1)
        
        return res
