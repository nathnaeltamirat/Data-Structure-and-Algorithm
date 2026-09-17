class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh_orange = 0
        row, col = len(grid), len(grid[0])
        direction = [(1,0),(0,1),(0,-1),(-1,0)]
        res = 0
        q = deque()
        def inBound(r,c):
            return r>=0 and c >= 0 and r < row and c <col
        for i in range(row):
            for j in range(col):
                val = grid[i][j]
                if val == 2:
                    q.append((i,j))
                elif val == 1:
                    fresh_orange += 1
        if fresh_orange == 0:
            return 0
        while q:
            n = len(q)
            for _ in range(n):
                i, j = q.popleft()
                for x, y in direction:
                    new_x = i + x
                    new_y = j + y
                    if inBound(new_x,new_y):
                        if grid[new_x][new_y] == 1:
                            fresh_orange -= 1

                            grid[new_x][new_y] = 2
                            q.append((new_x,new_y))
            res += 1
            if fresh_orange == 0:
                return res
            
        return -1

