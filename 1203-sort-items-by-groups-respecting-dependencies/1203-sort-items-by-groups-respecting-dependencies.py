class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        item_indegree = defaultdict(int)
        item_graph = defaultdict(list)
        group_indegree = defaultdict(int)
        group_graph = defaultdict(list)
        new_group = n
        for idx,g in enumerate(group):
            if g == -1:
                group[idx] = new_group
                new_group += 1

        for i in range(len(beforeItems)):
            for item in beforeItems[i]:
                item_indegree[i] += 1
                item_graph[item].append(i)
                if group[item] != group[i]:
                    group_graph[group[item]].append(group[i])
                    group_indegree[group[i]] += 1
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
            return order if len(order) == len(nodes) else []
        groups = list(range(new_group))
        grouped_item = bfs(group_graph,group_indegree,groups)
        if not grouped_item:
            return []
        items = list(range(n))
        ordered_item = bfs(item_graph,item_indegree,items)
        if not ordered_item:
            return []
        
        grouped_sorted_item = defaultdict(list)
        for item in ordered_item:
            grouped_sorted_item[group[item]].append(item)
        res = []
        for single_group in grouped_item:
            res.extend(grouped_sorted_item[single_group])
        return res