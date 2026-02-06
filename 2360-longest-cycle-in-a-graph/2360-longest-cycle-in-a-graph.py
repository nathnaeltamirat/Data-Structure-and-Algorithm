class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        indegree = defaultdict(int)
        q = deque()
        for i in range(len(edges)):
            if edges[i] != -1:
                indegree[edges[i]] += 1
        for i in range(len(edges)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            value = edges[node]
            if value != -1:
                indegree[value] -= 1
                if indegree[value] == 0:
                    q.append(value)
        res = -1
        visited = [False] * len(edges)
        for i in range(len(edges)):
            if indegree[i] > 0 and  not  visited[i]:
                count = 0
                node = i
                while not visited[node]:
                    visited[node] = True
                    count += 1
                    node = edges[node]
                res = max(res,count)
        return res
            
            