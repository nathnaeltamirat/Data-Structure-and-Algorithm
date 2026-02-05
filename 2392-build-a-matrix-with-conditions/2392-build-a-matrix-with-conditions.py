class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def bfs(graph,indegree,nodes):
            q = deque([node for node in nodes if indegree[node] == 0])
            order = []
            while q:
                item = q.popleft()
                order.append(item)
                for neigh in graph[item]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            return order if len(order) == len(nodes) else [] #cycle detected
        row_graph = defaultdict(list)
        row_indegree = defaultdict(int)
        col_graph = defaultdict(list)
        col_indegree = defaultdict(int)
    
        for a, b in rowConditions:
            row_graph[a].append(b)
            row_indegree[b] += 1
        for a ,b in colConditions:
            col_graph[a].append(b)
            col_indegree[b] += 1
        # print(col_graph)
        all_node = list(range(1,k+1))
        row_ordered = bfs(row_graph,row_indegree,all_node)
        if not row_ordered:
            return []
        col_ordered = bfs(col_graph,col_indegree,all_node)


        if not col_ordered:
            return []
        row = {num:i for i , num in enumerate(row_ordered)}
        col = {num: i for i , num in enumerate(col_ordered)}
        mat = [ [0]*k for _ in range(k)]
        print(row,col)
        for i in range(1,k+1):
            r = row[i]
            c = col[i]
            mat[r][c] = i
        print(mat)
        return mat
        # print(row_ordered)
        # print(col_ordered)

                    