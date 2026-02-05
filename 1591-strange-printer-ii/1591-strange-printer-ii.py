class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        count = defaultdict(int)
        row, column = len(targetGrid), len(targetGrid[0])
        color = {}
        for i in range(row):
            for j in range(column):
                val = targetGrid[i][j]
                if val not in color:
                    color[val] = [i,j,i,j]
                else:
                    color[val][0] = min(color[val][0],i) #top
                    color[val][1] = max(color[val][1],j) #right
                    color[val][2] = max(color[val][2],i) #bottom
                    color[val][3] = min(color[val][3],j) # left
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for c in color:
            top,right,bottom,left = color[c]
            for i in range(top,bottom+1):
                for j in range(left, right+ 1):
                    val = targetGrid[i][j]
                    if val != c:

                        graph[c].add(val)
        print(graph)
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node] != 1
            visited[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            visited[node] = 2
            return True
        for c in color:
            if c not in visited:
                if not dfs(c):
                    return False
        return True
        print(graph)