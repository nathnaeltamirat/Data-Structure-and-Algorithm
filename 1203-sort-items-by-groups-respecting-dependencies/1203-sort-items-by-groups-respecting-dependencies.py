class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        new_group = m
        group_graph = defaultdict(list)
        indegree_group = defaultdict(int)
        indegree_item = defaultdict(int)
        item_graph = defaultdict(list)
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = new_group
                new_group +=1

        def bfs(graph,indegree,nodes):
            q = deque([node for node in nodes if indegree[node] == 0])
            order = []
            while q:
                items = q.popleft()
                order.append(items)
                for neigh in graph[items]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
            return order if len(order) == len(nodes) else []

       
        for i in range(len(beforeItems)):
            for item in beforeItems[i]:
                if group[i] != group[item]:
                    group_graph[group[item]].append(group[i])
                    indegree_group[group[i]] +=1
                item_graph[item].append(i)
                indegree_item[i] += 1
        group_list = list(range(new_group))
        item_list = list(range(n))
        print(group_graph,indegree_group)
        groupped_order = bfs(group_graph,indegree_group,group_list)
        if not groupped_order:
            return []

        item_order = bfs(item_graph,indegree_item,item_list)
        if not item_order:
            return []
        print(groupped_order)
        group_holder = defaultdict(list)
        for item in item_order:
            group_holder[group[item]].append(item)
        res = []
        for i in groupped_order:
            res.extend(group_holder[i])
        print(res)
        return res
        