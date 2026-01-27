class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #bfs on each element that has a value of one will result in 
        #to get the desired result or distance

        row , column = len(mat), len(mat[0])
        queue = deque()
        visited = set()
        #checking weather or not is is bounde or not
        def bound(r,c):
            if r < 0 or c < 0 or r == row or c == column:
                return False
            return True
        
        #direction for top, right, bottom , left
        direction = [(-1,0),(0,1),(1,0),(0,-1)]

        def bfs():
            while queue:
                length = len(queue)
                for _ in range(length):
                    new_r, new_c = queue.popleft()
                    for i, j in direction:
                        dx = new_r + i
                        dy = new_c + j
                        if bound(dx,dy):
                            if (dx,dy) not in visited:
                                if mat[dx][dy] != 0:
                                    mat[dx][dy] = 1 + mat[new_r][new_c]
                                visited.add((dx,dy))   
                                queue.append((dx,dy))     
        for i in range(row):
            for j in range(column):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        bfs()
        return mat
