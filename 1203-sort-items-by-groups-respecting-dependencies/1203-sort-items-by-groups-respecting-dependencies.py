class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
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
            print("order",order)
            return order if len(order) == len(nodes) else []
        curr_group = max(group)
        for i in range(len(group)):
            if group[i] == -1:
                curr_group+=1
                group[i] = curr_group
        item_graph = defaultdict(list)
        item_indegree = defaultdict(int)
        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)
        all_elements = list(range(n))
        all_group = list(range(curr_group+1))
        for i in range(len(beforeItems)):
            for item in beforeItems[i]:
                item_indegree[i]+=1
                item_graph[item].append(i)
                if group[item] != group[i]:
                    group_graph[group[item]].append(group[i])
                    group_indegree[group[i]]+=1
        item_order = bfs(item_graph,item_indegree,all_elements)
       
        if not item_order:
            return []
        group_order = bfs(group_graph,group_indegree,all_group)
        print(curr_group,all_group,group,group_indegree)
        if not group_order:
            return []
        
        ordered_group = defaultdict(list)
        for i in item_order:
            g = group[i]
            ordered_group[g].append(i)
        print(item_order)
        print(group_order)
        print(ordered_group)
        res = []
        for g in group_order:
            res.extend(ordered_group[g])
        return res

        