class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()
        ans = []
        processed = 0
        if n <= 2:
            return list(range(n))

        #Inititalizing indegree
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        while q:
            length =  len(q)
            if n - processed <= 2:
                return list(q)
            for _ in range(length):
                node = q.popleft()
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:
                        q.append(neigh)
            processed += length

            