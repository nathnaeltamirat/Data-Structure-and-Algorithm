class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visited = set()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        res = -1
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < n and c < n
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if val == 1:
                    visited.add((i,j))
                    q.append((i,j))
        while q:
            i,j = q.popleft()
            for x, y in direction:
                new_x, new_y = i + x, j + y
                if inBound(new_x, new_y) and grid[new_x][new_y] == 0:
                    grid[new_x][new_y]  = 1 +  grid[i][j]
                    res = max(res,grid[new_x][new_y])
                    q.append((new_x,new_y))
        # print(grid)
        return res-1 if res != -1 else -1