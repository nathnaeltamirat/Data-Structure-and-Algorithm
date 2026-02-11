class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        row, column  = len(grid), len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        max_value = float('-inf')
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append((i,j))
                else:
                    grid[i][j] = -1
        # print(grid)
        while q:
            r, c = q.popleft()
            for x, y in direction:
                new_r = x + r
                new_c = y + c
                if inBound(new_r,new_c) and grid[new_r][new_c] == -1:
                    grid[new_r][new_c] = grid[r][c] + 1
                    max_value = max(max_value,grid[new_r][new_c])
                    q.append((new_r,new_c))
        print(grid)
        return max_value if max_value != float('-inf') else -1

