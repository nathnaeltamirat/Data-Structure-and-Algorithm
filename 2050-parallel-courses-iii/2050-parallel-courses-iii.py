class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in relations:
            graph[a].append(b)
            indegree[b] += 1
        q = deque()
        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)
        dp = [-1] * (n+1)

        while q:
            node = q.popleft()
            curr_time = time[node-1]
            dp[node] = max(dp[node],curr_time)
            for neigh in graph[node]:
                neigh_time = time[neigh-1]
                dp[neigh] = max(dp[neigh],neigh_time + dp[node])
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return max(dp)