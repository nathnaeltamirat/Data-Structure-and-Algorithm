class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        holder = defaultdict(list)
        row, col = len(targetGrid), len(targetGrid[0])
        all_elements = set()
        for i in range(row):
            for j in range(col):
                val = targetGrid[i][j]
                all_elements.add(val)
                if not holder[val]:
                    holder[val] = [i,j,i,j]
                else:
                    holder[val][0] = min(holder[val][0],i)#top
                    holder[val][1] = max(holder[val][1],j)#right
                    holder[val][2] = max(holder[val][2],i)#bottom
                    holder[val][3] = min(holder[val][3],j)#left
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in holder:
            top,right,bottom,left = holder[i]
            for j in range(top,bottom+1):
                for k in range(left,right+1):
                    val = targetGrid[j][k]
                    if val != i:
                        graph[i].append(val)
                        indegree[val] += 1
        q = deque()
        for item in list(all_elements):
            if indegree[item] == 0:
                q.append(item)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return count == len(all_elements)

             

