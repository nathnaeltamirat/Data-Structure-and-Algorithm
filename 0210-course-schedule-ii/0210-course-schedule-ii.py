class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        #intializer for origins
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        #Top sort algorithm
        while q:
            node = q.popleft()
            ans.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return ans if len(ans) == numCourses else []