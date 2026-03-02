class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        row, col = len(board), len(board[0])
        def inBound(r,c):
            return r >= 0 and c >= 0 and r < row and c < col
    
        direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        def bombCalculator(i,j):
            count = 0
            for x,y in direction:
                new_x = x + i
                new_y = y + j
                if inBound(new_x,new_y):
                    if board[new_x][new_y] == "M":
                        count += 1
            return count
    
        def dfs(i,j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return
            
            if board[i][j] == "E":
                val = bombCalculator(i,j)
                if val:
                    board[i][j] = str(val)
                    return
                else:
                    board[i][j] = "B"
            for x,y in direction:
                new_x = i + x
                new_y = y + j
                if inBound(new_x,new_y):
                    if board[new_x][new_y] == "E":
                        val = bombCalculator(new_x,new_y)
                        if val:
                            board[new_x][new_y] = str(val)
                        else:
                            board[new_x][new_y] = "B"
                            dfs(new_x,new_y)
    

        dfs(click[0],click[1])
        return board
                    
