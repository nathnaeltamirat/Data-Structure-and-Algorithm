class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,column = len(mat),len(mat[0])
        def inbound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        visited = set()
        def bfs():
            while q:
                n = len(q)
                for _ in range(n):
                    new_r, new_c = q.popleft()
                    for x, y in direction:
                        new_x = new_r + x
                        new_y = new_c + y
                        if inbound(new_x,new_y) and (new_x,new_y) not in visited:
                            if mat[new_x][new_y] != 0:
                                mat[new_x][new_y] = 1 + mat[new_r][new_c]
                            q.append((new_x,new_y))
                            visited.add((new_x,new_y))
        res = [ [0 for _ in range(column)] for _ in range(row)] 
        for i in range(row):
            for j in range(column):
                if mat[i][j] == 0:
                    q.append((i,j))
        bfs()
        return mat
                            
            