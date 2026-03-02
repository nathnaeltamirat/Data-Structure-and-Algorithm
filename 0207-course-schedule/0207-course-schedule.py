class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        def dfs(i):
            temp = True
            ans[i] = 0
            for neigh in graph[i]:
                if ans[neigh] == 0:
                    return False
                if ans[neigh] == -1:
                    temp = temp and dfs(neigh)
            ans[i] = 1
            return temp
        result = True
        ans = [-1] * numCourses
        for i in range(numCourses):
            if ans[i] == -1:
                result = result and dfs(i)
        print(graph)
        return result
