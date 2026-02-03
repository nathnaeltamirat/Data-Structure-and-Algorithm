class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a , b in prerequisites:
            graph[b].append(a)
        
        color = [-1] * numCourses
        def dfs(node):
            temp = True
            color[node] = 0
            for neigh in graph[node]:
                if color[neigh] == 0:
                    return False
                elif color[neigh] == -1:
                    temp = temp and dfs(neigh)
            color[node] = 1
            return temp
        result = True
        for i in range(numCourses):
            if color[i] == -1:
                result = result and dfs(i)
        return result
        

