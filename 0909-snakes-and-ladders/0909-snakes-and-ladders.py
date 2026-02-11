class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flattned = [-1] *(n * n)
        curr = 0
        res = -1
        ltor = True
        for i in range(n-1,-1,-1):
            col = range(0,n) if ltor else range(n-1,-1,-1)
            for j in col:
                if board[i][j] != -1:
                    flattned[curr] = board[i][j] - 1 
                curr+=1
            ltor = not ltor
        q = deque([0])
        visited = set([0])
        dist =  0
        target = n*n - 1
        while q:
            length = len(q)
            # print(q)
            for _ in range(length):
                curr = q.popleft()
                for i in range(curr + 1, min(curr + 6, (n ** n - 1)) + 1):
                    
                    val = flattned[i]
                    if val == target or i == target:
                        return dist + 1
                    if val !=  -1:
                        if val not in visited:
                            q.append(val)
                            visited.add(val)
                    else:
                        if i not in visited:
                            q.append(i)
                            visited.add(i)
            dist += 1
        return -1
                    


