class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        graph = [[[],[]] for _ in range(n)]
        q = deque([(0,0),(0,1)])
        visited = set([(0,0),(0,1)])

        for a,b in redEdges:
            graph[a][0].append(b)
        for a,b in blueEdges:
            graph[a][1].append(b)

        dist = 0
        while q:
            length = len(q)
            for _ in range(length):
                node,color = q.popleft()
                if ans[node] == -1:
                    ans[node] = dist
                alt = 1 - color
                for neigh in graph[node][alt]:
                    if (neigh,alt) not in visited:
                        q.append((neigh,alt))
                        visited.add((neigh,alt))
            dist += 1
        print(graph)
        print(ans)
        return ans