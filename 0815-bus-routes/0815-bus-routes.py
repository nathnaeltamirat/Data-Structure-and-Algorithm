class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        q = deque()
        visited = set()
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                if routes[i][j] == source:
                    q.append(i)
                    visited.add(i)
                graph[routes[i][j]].append(i)
        dist = 1
        while q:
            n = len(q)
            for _ in range(n):
                bus = q.popleft()
                for stop in routes[bus]:
                    if stop == target:
                        return dist 
                    for new_bus in graph[stop]:
                        if new_bus not in visited:
                            q.append(new_bus)
                            visited.add(new_bus)
                    graph[stop] = []
            dist += 1
        return -1
                        