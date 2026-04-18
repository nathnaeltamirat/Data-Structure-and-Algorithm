class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def bfs(graph,indegree,length):
            q = deque([item for item in length if indegree[item] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            return order if len(order) == len(length) else []
        row_graph = defaultdict(list)
        row_indegree = defaultdict(int)
        for a,b in rowConditions:
            row_graph[a].append(b)
            row_indegree[b] += 1
        row_order = bfs(row_graph,row_indegree,range(1,k+1))
        if not row_order:
            return []
        col_graph = defaultdict(list)
        col_indegree = defaultdict(int)
        for a,b in colConditions:
            col_graph[a].append(b)
            col_indegree[b] += 1
        col_order = bfs(col_graph,col_indegree,range(1,k+1))
        if not col_order:
            return []
        # print(row_order)
        # print(col_order)
        res = [[0] * k for _ in range(k)]
        print(res)
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        for i in range(k):
            row_dict[row_order[i]] = i
            col_dict[col_order[i]] = i
        # print(row_dict)
        # print(col_dict)
        for i in range(1,k+1):
            r = row_dict[i]
            c = col_dict[i]
            res[r][c] = i
        return res

