class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()

        for prev_course,next_course in relations:
            graph[prev_course].append(next_course)
            indegree[next_course] += 1
        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)
        dp = [-1] * (n+1)

        while q:
            length = len(q)
            print(q)
            for _ in range(length):
                curr_course = q.popleft()
                curr_time = time[curr_course-1]
                dp[curr_course] = max(dp[curr_course],curr_time)
                for neigh in graph[curr_course]:
                    dp[neigh] = max(dp[neigh],dp[curr_course] + time[neigh - 1])
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
        return max(dp)

