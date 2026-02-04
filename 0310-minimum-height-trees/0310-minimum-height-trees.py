class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        degree = defaultdict(int)
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        remaining = n   
        while remaining > 2:
            n = len(q)
            remaining -= n
            for _ in range(n):
                node = q.popleft()
                for neigh in graph[node]:
                    degree[neigh] -= 1
                    if degree[neigh] == 1:
                        q.append(neigh)
        return list(q)