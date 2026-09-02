class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        #initialize
        graph = defaultdict(set)
        indegree = defaultdict(int)
        holder = defaultdict(list)
        row, col = len(targetGrid), len(targetGrid[0])
        elements = set()
        q = deque()

        #finding the square position
        for i in range(row):
            for j in range(col):
                val = targetGrid[i][j]
                elements.add(val)
                if not holder[val]:
                    holder[val] = [i,j,i,j] #clock wise direction
                else:
                    holder[val][0] = min(holder[val][0],i) #Top
                    holder[val][1] = max(holder[val][1],j) #right
                    holder[val][2] = max(holder[val][2],i) #Bottom
                    holder[val][3] = min(holder[val][3],j) #left
            
        
        elements = list(elements)
        for i in range(len(elements)):
            top,right,bottom,left = holder[elements[i]]
            original = elements[i]
            for i in range(top,bottom+1):
                for j in range(left,right+1):
                    val = targetGrid[i][j]
                    if val != original and val not in graph[original]:
                        graph[original].add(val)
                        indegree[val] += 1
        for el in elements:
            if indegree[el] == 0:
                q.append(el)
        checker = 0
        while q:
            node = q.popleft()
            checker += 1
            for neigh in list(graph[node]):
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return checker == len(elements)