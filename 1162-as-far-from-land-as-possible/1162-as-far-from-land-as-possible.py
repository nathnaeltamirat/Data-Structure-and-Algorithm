class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
      #0 - water 
      #1 - land  

        visited = set()
        q = deque()
        row, column = len(grid), len(grid[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        res = float('-inf')
        water = False
        def inbound(r,c):
            return r>=0 and r < row and c >= 0 and c < column

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
                    grid[i][j] = 0
                else:
                    water = True
        if not q or not water:
            return -1

        while q:
            r, c = q.popleft()
            for x,y in direction:
                new_r = x + r
                new_c = y + c
                if inbound(new_r,new_c) and (new_r,new_c) not in visited:
                    visited.add((new_r,new_c))
                    q.append((new_r,new_c))
                    grid[new_r][new_c] = grid[r][c] + abs(new_r - r) + abs(new_c - c)

                    res = max(res,grid[new_r][new_c])
        return res