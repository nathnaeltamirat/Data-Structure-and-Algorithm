class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_bus = defaultdict(list)
        q = deque()
        visited = set()
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                stop = routes[i][j]
                stop_to_bus[stop].append(i)
                if stop == source:
                    q.append(i)
                    visited.add(i)

        print(q)
        if source == target:
            return 0
        dist = 0
        while q:
            n = len(q)
            for _ in range(n):
                bus = q.popleft()
                for route in routes[bus]:
                    if route  == target:
                        return dist + 1
                    for new_bus in stop_to_bus[route]:
                        if new_bus not in visited:
                            q.append(new_bus)
                            visited.add(new_bus)
                    stop_to_bus.pop(route)
            dist += 1
        return -1
            