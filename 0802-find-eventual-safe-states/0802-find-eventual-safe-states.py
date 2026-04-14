class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjecency = defaultdict(list)
        outdegree = defaultdict(int)
        for i in range(len(graph)):
            for item in graph[i]:
                adjecency[item].append(i)
                outdegree[i]+=1
        q = deque()
  
        for i in range(len(graph)):
            if outdegree[i] == 0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for neigh in adjecency[node]:
                outdegree[neigh] -= 1
                if outdegree[neigh] == 0:
                    q.append(neigh)
        return sorted(res)