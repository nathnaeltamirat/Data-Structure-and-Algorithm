class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        courses =set()
        for a ,b in prerequisites:
            graph[b].append(a)
            courses.add(a)
            courses.add(b)
            indegree[a] += 1
        if not prerequisites:
            return True

        
        no_cycle = True

        color = [0] * numCourses
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
            color[node] = 1
            for neigh in graph[node]:
                if color[neigh] == 1:
                    no_cycle = False
                    break
                elif color[neigh] == 0:
                    dfs(neigh)
            
            color[node] = 2

        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)

        print(no_cycle)
        return no_cycle 
            
