class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_orange = 0
        fresh_orange = 0
        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        row, column = len(grid),len(grid[0])

        def inbound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column

        q = deque()
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 2:
                    rotten_orange += 1
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_orange += 1


        if fresh_orange == 0:
            return 0

        res = 0
        while q:
            n = len(q)
            res += 1
            for _ in range(n):
                
                r, y = q.popleft()
                for dx, dy in direction:
                    new_r = dx + r
                    new_y = dy + y
                    if inbound(new_r, new_y) and grid[new_r][new_y] == 1:
                        q.append((new_r,new_y))
                        grid[new_r][new_y] = 2
                        fresh_orange -= 1
                    if fresh_orange == 0:
                        return res
        return -1
