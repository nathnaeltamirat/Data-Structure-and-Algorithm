class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        order = defaultdict(set)
        q = deque()
        ans = []

        #Creating relationship graph
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        #Finding the required course first
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        #Finding prerequisite relation
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                order[neigh].add(node)
                order[neigh].update(order[node])
                if indegree[neigh] == 0:
                    q.append(neigh)
        for a, b in queries:
            if a in order[b]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        