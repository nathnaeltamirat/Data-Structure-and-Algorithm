class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        color = defaultdict(list)
        row, column = len(targetGrid), len(targetGrid[0])
        indegree = defaultdict(int)
        graph = defaultdict(set)
        all_elements = set()
        for i in range(row):
            for j in range(column):
                value = targetGrid[i][j]
                if value not in color:
                    color[value] = [i,j,i,j]
                else:
                    color[value][0] = min(color[value][0],i)#top
                    color[value][1] = max(color[value][1],j)#right
                    color[value][2] = max(color[value][2],i)#bottom
                    color[value][3] = min(color[value][3],j)#left
                all_elements.add(value)
        all_elements = list(all_elements)
        for i in color:
            top,right ,bottom,left = color[i]
            for r in range(top,bottom+1):
                for c in range(left,right+1):
                    val = targetGrid[r][c]
                    if i != val:
                        if val not in graph[i]:
                            graph[i].add(val)
                            indegree[val]+=1
        q = deque([node for node in color if indegree[node] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return True if len(res) == len(all_elements) else False
        print(q)
        
