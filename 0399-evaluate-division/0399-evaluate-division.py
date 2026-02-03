class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        elements = set()
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            graph[a].append([b,value])
            graph[b].append([a,1/value])
            elements.add(a)
            elements.add(b)
        
        res = []
        visited = set()
        def dfs(src,dest):
            if src == dest:
                return 1
            visited.add(src)
            for neigh,curr_val in graph[src]:
                if neigh not in visited:
                    val = dfs(neigh,dest)
                    if val != -1:
                        return val * curr_val
                    
            return -1 
        
        print(graph)
        for a,b in queries:
            if a  not in elements or b not in elements:
                res.append(-1)
            else:
                visited = set()
                print(a,b)
                res.append(dfs(a,b))
        return res
