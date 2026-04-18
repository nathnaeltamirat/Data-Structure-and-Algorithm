class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()
        for i in range(len(edges)):
            if edges[i]!= -1:
                graph[i].append(edges[i])
                indegree[edges[i]]+=1
        for i in range(len(edges)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        res =  - 1
        for i in range(len(edges)):
            if indegree[i] > 0 and edges[i] != -1:
                node = i
                curr = 0
                while edges[node] != -1:
                    curr += 1
                    prev = node
                    node = edges[node]
                    edges[prev] = -1
                res = max(res,curr)
        return res
