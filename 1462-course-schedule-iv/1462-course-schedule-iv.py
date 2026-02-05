class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        res = [False] * len(queries)
        q = deque()
        holder = defaultdict(set)

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                holder[neigh].update(holder[node])
                holder[neigh].add(node)
                if indegree[neigh] == 0:
                    q.append(neigh)
        for i in range(len(queries)):
            a, b = queries[i]
            if a in holder[b]:
                res[i] = True
            else:
                res[i] = False
        return res