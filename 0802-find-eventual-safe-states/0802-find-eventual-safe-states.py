class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal_nodes = set()
        res = []
        color = [-1] * len(graph)

        
        #detetc cycle
        def dfs(node):
            if color[node] != -1:
                return color[node] == 1
            color[node] = 0
            for neigh in graph[node]:
                if color[neigh] == 0 or not dfs(neigh) :
                    color[node] = 2
                    return False
             
            color[node] = 1
            return True
        for i in range(len(graph)):
            dfs(i)
        print(res)
        return [i for i in range(len(color)) if color[i] == 1]
        print(color)
