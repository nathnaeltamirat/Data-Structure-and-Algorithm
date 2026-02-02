class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        color = [-1] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        def dfs(node):
            val = True
            for neigh in graph[node]:
                if color[neigh] == -1:
                    color[neigh] = 0
                    val = val and dfs(neigh)
                elif color[neigh] == 0:
                    val = False
            color[node] = 2
            return val
        for i in range(numCourses):
            if color[i] == -1:
                if not dfs(i):
                    return False
        return True
