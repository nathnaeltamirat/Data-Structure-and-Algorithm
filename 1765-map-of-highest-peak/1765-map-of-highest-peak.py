class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row, col = len(isWater), len(isWater[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        visited = set()
        def inBound(r,c):
            return r>= 0 and c >= 0 and r < row and c < col
        for i in range(row):
            for j in range(col):
                val = isWater[i][j]
                if val == 1:
                    isWater[i][j] = 0
                    q.append((i,j))
                    visited.add((i,j))
                else:
                    isWater[i][j] = 1
        while q:
            r, c = q.popleft()
            for x, y in direction:
                new_x = x + r
                new_y = y + c
                if inBound(new_x,new_y) and (new_x,new_y) not in visited:
                    q.append((new_x,new_y))
                    visited.add((new_x,new_y))
                    isWater[new_x][new_y] += isWater[r][c]
        return isWater
