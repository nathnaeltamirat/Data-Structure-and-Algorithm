class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topSort(nodes,graph,indegree):
            q = deque([node for node in nodes if indegree[node] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            return order if len(order) == len(nodes) else []
        #initialization
        mat = [[0] * k for _ in range(k)]
        row_graph = defaultdict(list)
        row_indegree = defaultdict(int)
        col_graph = defaultdict(list)
        col_indegree = defaultdict(int)
        for a, b in rowConditions:
            row_graph[a].append(b)
            row_indegree[b] += 1
        for a,b in colConditions:
            col_graph[a].append(b)
            col_indegree[b] += 1
        
        row_order = topSort(range(1,k+1),row_graph,row_indegree)
     
        if not row_order:
            return []
        print(row_order)
        col_order = topSort(range(1,k+1),col_graph,col_indegree)
        if not col_order:
            return []
        row_order1 = defaultdict(int)
        col_order1 = defaultdict(int)
        for i in range(k):
            row_order1[row_order[i]] = i
            col_order1[col_order[i]] = i
        for i in range(1,k+1):
            r = row_order1[i]
            c = col_order1[i]
            mat[r][c] = i

        
        return mat