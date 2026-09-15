class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = len(board), len(board[0])
        direction = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1)]
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < col
        
        def dfs(i,j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return
            count = 0
            for x, y in direction:
                new_x, new_y = x + i, y + j
                if inBound(new_x,new_y):
                    if board[new_x][new_y] == "M":
                        count += 1
                
            if count:
                board[i][j] = str(count)
            else:
                board[i][j] = "B"
                for x, y in direction:
                    new_x, new_y = x + i, y + j
                    if inBound(new_x,new_y):
                        if board[new_x][new_y] == "E":
                            dfs(new_x,new_y)
                            
        dfs(click[0],click[1])
        return board
