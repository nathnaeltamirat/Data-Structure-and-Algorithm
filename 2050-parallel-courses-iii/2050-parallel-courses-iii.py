class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()
        for a, b in relations:
            graph[a].append(b)
            indegree[b] += 1
        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)
        
        dp = [0] * n
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                dp[neigh-1] = max(dp[neigh-1], dp[node-1] +  time[node-1] )
                indegree[neigh] -=1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return max(dp[i] + time[i] for i in range(n))
