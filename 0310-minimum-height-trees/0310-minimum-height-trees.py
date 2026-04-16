class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        connection = defaultdict(int)
        q = deque()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            connection[a] += 1
            connection[b] += 1
        for i in range(n):
            if connection[i] == 1:
                q.append(i)
        current = n
        print(q)
        while q and  current > 2:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                current -= 1
                for neigh in graph[node]:
                    connection[neigh] -= 1
                    if connection[neigh] == 1:
                        q.append(neigh)
        return list(q)
