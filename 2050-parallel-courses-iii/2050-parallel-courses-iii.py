class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()
        dp = [0] * (n + 1)
        for pre_course, next_course in relations:
            nxt_time = time[next_course-1]
            graph[pre_course].append([next_course,nxt_time])
            indegree[next_course] += 1
        
        for course in range(1,n+1):
            if indegree[course] == 0:
                c_time = time[course-1]
                q.append([course,c_time])
                dp[course] = c_time
        print(graph)
        
        res = 0
        while q:
            n = len(q)
            max_time = 0
            print(q)
            #parallel course
            for _ in range(n):
                course, curr_time = q.popleft()
                max_time = max(curr_time,max_time)
                for next_course,next_time in graph[course]:
                    dp[next_course] = max(dp[next_course],next_time + dp[course])
                    indegree[next_course] -= 1
                    #no prerequistes of course indegree -> 0
                    if indegree[next_course] == 0:
                        q.append((next_course,next_time))

            res += max_time
        return max(dp)
        