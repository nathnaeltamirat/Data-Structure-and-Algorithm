class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        ans = True
        def dfs(node):
            nonlocal ans
            for neigh in graph[node]:
                if color[neigh] == -1:
                    color[neigh] = 1 - color[node]
                    dfs(neigh)
                elif color[neigh] == color[node]:
                    ans = False
                    return False
        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                dfs(node)
            
          
        
        
                
        return ans
            
            

