class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        #Top Sort algorithm

        def bfs(nodes,indegree,graph):
            q = deque([node for node in nodes if indegree[node] == 0  ])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            return order if len(order) == len(nodes) else []
        node_graph = defaultdict(list)
        node_indegree = defaultdict(int)
        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)

        #For groups with no group
        ne_group = max(group) + 1
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = ne_group
                ne_group+=1

        for i in range(len(beforeItems)):
            for j in range(len(beforeItems[i])):
                node_indegree[i] += 1
                node_graph[beforeItems[i][j]].append(i)
                if group[i] != group[beforeItems[i][j]]:
                    group_graph[group[beforeItems[i][j]]].append(group[i])
                    group_indegree[group[i]] += 1
        

        group_order = bfs(list(range(0,ne_group)),group_indegree,group_graph)

        #cycle detected
        if not group_order:
            return []
      
        node_order = bfs(list(range(n)),node_indegree,node_graph)
        #cycle detected
        if not node_order:
            return []
       
        #printing in the correct format
        group_ordered = defaultdict(list)
        res = []
        for i in node_order:
            group_ordered[group[i]].append(i)
     
        for i in group_order:
            res.extend(group_ordered[i])
        return res
