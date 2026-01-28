class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        #multi source bfs
        q = deque()
        visited = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        row , column = len(isWater), len(isWater[0])

        def inbound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column

        for i in range(row):
            for j in range(column):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = 1
        
        while q:
            r, c = q.popleft()
            for x,y in directions:
                new_r = x + r
                new_c = y + c
                if inbound(new_r,new_c) and (new_r,new_c) not in visited:
                    if isWater[r][c] == 0:
                        isWater[new_r][new_c] = 1
                    else:
                        isWater[new_r][new_c] = isWater[r][c] +1

                    visited.add((new_r,new_c))
                    q.append((new_r,new_c))
        return isWater
                    