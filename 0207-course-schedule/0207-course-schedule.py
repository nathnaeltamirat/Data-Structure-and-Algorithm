class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #doing graph
        ans = True
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        color = [-1] * numCourses

        def dfs(i):
            nonlocal ans
            color[i] = 0
            for neigh in graph[i]:
                if color[neigh] == 0:
                    ans = False
                elif color[neigh] == -1:
                    dfs(neigh)
            color[i] = 1

        for i in range(numCourses):
                dfs(i)
        return ans