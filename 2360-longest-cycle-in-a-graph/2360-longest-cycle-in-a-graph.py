class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        indegree = defaultdict(int)
        for i in range(len(edges)):
            val = edges[i]
            indegree[val] += 1
        q = deque([node for node in range(len(edges)) if indegree[node] == 0])
        while q:
            node = q.popleft()
            neigh = edges[node]
            if neigh != -1:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
            

  
        visited = [False] * len(edges)
        res = -1
        for i in range(len(edges)):
            if not visited[i] and indegree[i] > 0:
                
                curr = 0
                node = i
                while node != -1 and not visited[node]:
                    curr += 1
                    visited[node] = True
                    node = edges[node]

                res = max(res,curr)
        return res
