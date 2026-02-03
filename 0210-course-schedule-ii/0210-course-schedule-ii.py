class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        res = []

        def dfs(node):
            if indegree[node] == 0:
                indegree[node] -= 1
                res.append(node)
            for neigh in graph[node]:
                if indegree[neigh] > 0:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        dfs(neigh)

        for a in range(numCourses):
            if indegree[a] == 0:
                dfs(a)
        return res if len(res) == numCourses else []

        