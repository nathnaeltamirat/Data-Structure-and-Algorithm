class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        row, column = len(targetGrid), len(targetGrid[0])
        graph = defaultdict(list)
        indegree = defaultdict(int)
        holder = defaultdict(list)
        q = deque()
        all_elements = set()
        for i in range(row):
            for j in range(column):
                val = targetGrid[i][j]
                all_elements.add(val)
                if val not in holder:
                    holder[val] = [i,j,i,j] #top right bottom left
                else:
                    holder[val][0] = min(i,holder[val][0]) #top
                    holder[val][1] = max(j,holder[val][1]) #right
                    holder[val][2] = max(i,holder[val][2]) #bottom
                    holder[val][3] = min(j,holder[val][3]) #left
        for node in holder:
            top,right,bottom,left = holder[node]
            for i in range(top,bottom+1):
                for j in range(left,right+1):
                    val = targetGrid[i][j]
                    if val != node and val not in graph[node]:
                        graph[node].append(val)
                        indegree[val] += 1
        
        all_elements = list(all_elements)
        for i in all_elements:
            if indegree[i] == 0:
                q.append(i)
            
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neigh in graph[node]:
                indegree[neigh] -=1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return True if len(order) == len(all_elements) else False

        