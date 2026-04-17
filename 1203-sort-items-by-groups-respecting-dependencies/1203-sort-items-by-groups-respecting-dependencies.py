class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def bfs(indegree,graph,length):
            q = deque([item for item in length if indegree[item] == 0])
            order = []
            while q:
                node =q.popleft()
                order.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            return order if len(order) == len(length) else []
        max_group = max(group)
        for i in range(len(group)):
            if group[i] == -1:
                max_group += 1
                group[i] = max_group
        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)
        for i in range(len(beforeItems)):
            for item in beforeItems[i]:
                if group[item] != group[i]:
                    group_graph[group[item]].append(group[i])
                    group_indegree[group[i]] += 1

        group_order = bfs(group_indegree,group_graph,range(max_group+1))
        if not group_order:
            return []
        item_graph = defaultdict(list)
        item_indegree = defaultdict(int)
        for i in range(len(beforeItems)):
            for item in beforeItems[i]:
                item_graph[item].append(i)
                item_indegree[i] += 1
        item_order = bfs(item_indegree,item_graph,range(n))
        if not item_order:
            return []
        # print(group_order,item_order)
        order = defaultdict(list)
        res = []
        for j in item_order:
            order[group[j]].append(j)
        for g in group_order:
            res.extend(order[g])
        return res
