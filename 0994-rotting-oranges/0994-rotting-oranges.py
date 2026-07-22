class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        row , col = len(grid), len(grid[0])
        def inBound(r,c):
            return r >= 0 and c>= 0 and r < row and c < col
        fresh_orange  = 0
        q = deque()
        res = 0
        for i in range(row):
            for j in range(col):
                val = grid[i][j]
                if val == 2:
                    q.append((i,j))
                elif val == 1:
                    fresh_orange +=1
        if fresh_orange == 0:
            return 0

 
        while q:
            n = len(q)
            print(q)
            for _ in range(n):
                r, c = q.popleft()
                for x, y in direction:
                    new_x = x + r
                    new_y = y + c
                    if inBound(new_x,new_y) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        q.append((new_x,new_y))
                        fresh_orange -= 1
            res += 1
            
        return res-1 if fresh_orange == 0 else -1