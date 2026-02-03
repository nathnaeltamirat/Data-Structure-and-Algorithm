class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        row , column = len(board), len(board[0])
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column
        
        def bombFinder(i,j):
            count = 0
            for x,y in direction:
                new_x = i + x
                new_y = j + y
                if inBound(new_x,new_y) and board[new_x][new_y] == "M":
                    count += 1
            return count
        def dfs(i,j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return
            elif board[i][j] == "E":
                count = bombFinder(i,j)
                if count:
                    board[i][j] = str(count)
                    return
                else:
                    board[i][j] = "B"
            for x,y in direction:
                new_x = i + x
                new_y = j + y
                if inBound(new_x,new_y):
                    if board[new_x][new_y] == "E":
                        count = bombFinder(new_x,new_y)
                        if count:
                            board[new_x][new_y] = str(count)
                        else:
                            board[new_x][new_y] = "B"
                            dfs(new_x,new_y)
        dfs(click[0],click[1])
        print(board)
        return board