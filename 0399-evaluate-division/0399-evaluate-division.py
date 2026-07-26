class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        variables = set()
        visited = set()
        for i in range(len(equations)):
            variables.add(equations[i][0])
            variables.add(equations[i][1])
            graph[equations[i][0]].append([equations[i][1],values[i]])
            graph[equations[i][1]].append([equations[i][0],1/values[i]])
       
        res = 0
        def dfs(src,dest):
            visited.add(src)
            if src == dest:
                return 1
            for neigh, val in graph[src]:
                if neigh not in visited:
                    value = val * dfs(neigh,dest)
                    if value:
                        return value
            return 0
        ans = []
        for a, b in queries:
            if a not in variables or b not in variables:
                ans.append(-1)
            else:
                visited = set()
                val = dfs(a,b)
                if val == 0:
                    ans.append(-1)
                else:
                    ans.append(val)
        return ans
