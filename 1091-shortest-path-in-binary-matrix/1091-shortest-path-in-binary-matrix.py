class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
        grid[0][0] = 1
        row = column = len(grid)
        direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        q = deque([(0,0)])
        dist = 1

        def inbound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column

        while q:
            n = len(q)
            dist += 1
            for _ in range(n):
                r, c = q.popleft()
                for x, y in direction:
                    new_x = x + r
                    new_y = y + c
                    if inbound(new_x,new_y) and grid[new_x][new_y] == 0:
                        print(new_x,new_y,)
                        grid[new_x][new_y] = 1
                        q.append((new_x,new_y))
                        if new_x == row-1 and new_y == column-1:
                            return dist
            
            print(dist)
        return -1




        