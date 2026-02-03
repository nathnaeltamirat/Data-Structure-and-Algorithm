class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        hasher = defaultdict(set)
        indegree = defaultdict(int)
        q = deque()
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                hasher[neigh].add(node)
                hasher[neigh].update(hasher[node])
                if indegree[neigh] == 0:
                    q.append(neigh)
        res = []
        for a,b in queries:
            if b in hasher[a]:
                res.append(True)
            else:
                res.append(False)
        print(res)
        print(hasher)
        return res