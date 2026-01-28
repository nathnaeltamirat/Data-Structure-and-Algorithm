class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #constructing new grid
        n = len(board)
        formatted  = [-1] * (n * n) 
        visited = set([0])
        ltor = True
        target = ((n*n)-1)
        q = deque([0])
        curr = 0
        for i in range(n-1,-1,-1):
            cols = range(n) if ltor else  range(n-1,-1,-1)
            for j in cols:
                if board[i][j] != -1:
                    formatted[curr] = board[i][j] - 1
                curr += 1
            ltor = not  ltor

        dist = 1
        while q:
            l = len(q)
            for _ in range(l):
                idx = q.popleft()
                for i in range(idx + 1, min(idx + 6, (n**2 -1 )) + 1):
                    val = formatted[i]
                    if i ==  target or val == target:
                        return dist
                    if val!= -1:
                        if val not in visited:
                            q.append(val)
                            visited.add(val)
                    else:
                        if i not in visited:
                            q.append(i)
                            visited.add(i)
            dist += 1
        return - 1
