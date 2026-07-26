class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        ans = True
        def dfs(node):
            nonlocal ans
            for neigh in graph[node]:
                if color[neigh] == -1:
                    color[neigh] = 1 - color[node]
                    if not dfs(neigh):
                        return False
                elif color[neigh] == color[node]:
                    ans = False
                    return False
            return True
        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        return True
            
          
        
        
                
        return ans
            
            
