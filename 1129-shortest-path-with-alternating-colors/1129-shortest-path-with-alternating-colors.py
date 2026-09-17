class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        ans = [-1] * n
        graph = [[[],[]] for _ in range(n)]
        for a,b in redEdges:
            graph[a][0].append(b)
        for a, b in blueEdges:
            graph[a][1].append(b)
        q = deque([[0,0],[0,1]])
        visited = set(((0,0),(0,1)))
        dist = 0
        while q:
            n = len(q)
            for _ in range(n):
                node , color = q.popleft()
                if ans[node] == -1:
                    ans[node] = dist
                alt = 1 - color
                for neigh in graph[node][alt]:
                    if (neigh,alt) not in visited:
                        q.append((neigh,alt))
                        visited.add((neigh,alt))

            dist += 1
        return ans