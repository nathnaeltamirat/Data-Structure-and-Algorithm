class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #cycle detection  can be done using topsort i think but 
        #lets do cycle detection
        graph = defaultdict(list)
        color = [-1] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
        
        def dfs(node):
            color[node] = 0
            for neigh in graph[node]:
                if color[neigh] == 0:
                    return False
                if color[neigh] != 1 and not dfs(neigh):
                    return False
            color[node] = 1
            return True
        res = True
        for i in range(numCourses):
            if color[i] == -1:
                res = res and dfs(i)
                if not res:
                    return False
        return True        