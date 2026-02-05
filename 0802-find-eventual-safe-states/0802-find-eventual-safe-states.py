class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dependency_graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()

        for i in range(len(graph)):
            for node in graph[i]:
                dependency_graph[node].append(i)
                indegree[i] += 1
        res = [] 
        for i in range(len(graph)):
            if indegree[i] == 0:
                q.append(i)

         
        while q:
            node = q.popleft()
            res.append(node)
            for neigh in dependency_graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return sorted(res)