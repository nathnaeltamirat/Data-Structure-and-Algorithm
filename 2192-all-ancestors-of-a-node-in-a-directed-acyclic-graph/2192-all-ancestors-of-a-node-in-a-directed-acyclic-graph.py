class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        res = [set() for _ in range(n)]
        q = deque()

        for a , b in edges:
            graph[a].append(b)
            indegree[b] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        print(q)
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                for neigh in graph[node]:
                    indegree[neigh]-=1
                    res[neigh].update(res[node])
                    res[neigh].add(node)    
                    if  indegree[neigh] == 0:
                        q.append(neigh)
        
        return [sorted(lst) for lst in res]