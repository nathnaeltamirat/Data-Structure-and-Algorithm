class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        row, col = len(isWater), len(isWater[0])
        visited = set()
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < row and c < col
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
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
            i,j = q.popleft()
            for x, y in direction:
                new_x, new_y = i + x, j + y
                if inBound(new_x,new_y) and (new_x,new_y) not in visited:
                        visited.add((new_x,new_y))
                        q.append((new_x,new_y))
                        isWater[new_x][new_y] += isWater[i][j]
        return isWater