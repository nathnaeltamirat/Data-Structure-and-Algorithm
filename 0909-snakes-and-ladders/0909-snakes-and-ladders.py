class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        fragmented = [-1] * (n * n)
        ltor = True
        target = (n*n) - 1
        idx = 0
        for i in range(n-1,-1,-1):
            j = range(n) if ltor else range(n-1,-1,-1)
            for k in j:
                if board[i][k] != -1:
                    fragmented[idx] = board[i][k] - 1
                idx+=1
            ltor = not ltor
        
        q = deque([0])
        visited = set([0])
        dist = 1
        while q:
            t = len(q)
            for _ in range(t):
                curr = q.popleft()
                for i in range(curr + 1,min(curr+7,n**n)):
                    if i == target or  fragmented[i] == target:
                        return dist
                    if fragmented[i] == -1:
                        if i not in visited:
                            visited.add(i)
                            q.append(i)
                    else:
                        if fragmented[i] not in visited:
                            visited.add(fragmented[i])
                            q.append(fragmented[i])
            dist += 1
                        
        print(fragmented)
        print(dist)
        return -1