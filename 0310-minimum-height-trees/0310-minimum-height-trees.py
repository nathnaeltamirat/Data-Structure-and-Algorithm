class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        q = deque()
        graph = defaultdict(list)
        indegree = defaultdict(int)

        if not edges:
            res = []
            for i in range(n):
                res.append(i)
            return res
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        size = n
        while q:
            length = len(q)
            
            if size <= 2:
                break
            for _ in range(length):
                node = q.popleft()
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:

                        q.append(neigh)
            size -= length
        print(q)
        return list(q)