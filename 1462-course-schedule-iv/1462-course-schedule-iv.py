class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a,b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        q = deque()
        res = defaultdict(set)
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                res[neigh].update(res[node])
                res[neigh].add(node)
                if indegree[neigh] == 0:

                    q.append(neigh)
        
        ans = []
        for a,b in queries:
            if a in res[b]:
                ans.append(True)
                continue
            ans.append(False)
   
        return ans