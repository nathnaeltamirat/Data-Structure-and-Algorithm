class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def bfs(graph,indegree,nodes):
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
        row_graph = defaultdict(list)
        column_graph = defaultdict(list)
        row_indegree = defaultdict(int)
        column_indegree = defaultdict(int)
        for a, b in rowConditions:
            row_graph[a].append(b)
            row_indegree[b] += 1
        for a, b in colConditions:
            column_graph[a].append(b)
            column_indegree[b] += 1
        all_nodes = list(range(1,k+1))
        row_order = bfs(row_graph,row_indegree,all_nodes)
        if not row_order:
            return []
        column_order = bfs(column_graph,column_indegree,all_nodes)
        if not column_order:
            return []
        row_pos = {row_order[i]: i for i in range(len(row_order))}
        col_pos = {column_order[i]: i for i in range(len(column_order)) }
        matrix = [[0] * k for _ in range(k)]
        for i in range(1,k+1):
            r = row_pos[i]
            c = col_pos[i]
            matrix[r][c] = i
        print(matrix)
        print(row_order)
        print(column_order)
        return matrix
        