class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q =deque([(0,0),(0,1)])

        visited = set(((0,0),(0,1)))
        graph = [[[],[]] for _ in range(n)]
        ans = [-1] * n
        for a, b in redEdges:
            graph[a][0].append(b)
        for a, b in blueEdges:
            graph[a][1].append(b)
        dist = 0
        print(graph)
        while q:
            n = len(q)
            print(q)
            for _ in range(n):
                node, color = q.popleft()
                if ans[node] == -1:
                    ans[node] = dist
                alternative = 1 - color
                for neigh in graph[node][alternative]:
                    if (neigh,alternative) not in visited:
                        visited.add((neigh,alternative))
                        q.append((neigh,alternative))
   
            dist += 1
        return ans
                