class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row , column = len(maze), len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque([(entrance[0],entrance[1])])
        maze[entrance[0]][entrance[1]] = "+"
        dist = 1
        found = False

        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column
        def isExit(r,c):
            ## in border
            return ( r == 0 or r == row - 1 or c == 0 or c == column-1)

        while q:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                for x, y in directions:
                    new_r = x + r
                    new_c = y + c
                    if inBound(new_r,new_c) and maze[new_r][new_c] == ".":
                        if isExit(new_r,new_c):
                            found = True
                            return dist
                        maze[new_r][new_c] = "+"
                        q.append((new_r,new_c))
            dist += 1
        if not found:
            return -1
        return dist


