class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        elements =set()
        graph = defaultdict(list)
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]
            graph[a].append([b,value])
            graph[b].append([a,1/value])
            elements.add(a)
            elements.add(b)
        print(graph)
        res = []
        def dfs(a,b,visited,curr):
            visited.add(a)
            if a == b:
                return 1

            for neigh, c_val in graph[a]:
                if neigh not in visited:
                    if neigh == b:
                        return curr * c_val
                    val = dfs(neigh,b,visited,c_val * curr)
                    if val != -1:
                        return val
                    
            return -1
        for a,b in queries:
  
            if  a not in elements  or b not in elements:
                res.append(-1)

            else:
                res.append(dfs(a,b,set(),1))

        return res