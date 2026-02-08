class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(lambda: 1)
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dsu = UnionFind()
        direction = {
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]
        }
        row, column = len(grid),len(grid[0])
        def inBound(r,c):
            return r >= 0 and r < row and c >= 0 and c < column
        
        for i in range(row):
            for j in range(column):
                val = grid[i][j]
                for x, y in direction[val]:
                    new_x = x + i
                    new_y = y + j
                    if inBound(new_x,new_y):
                        new_grid = grid[new_x][new_y]
                        if (-x,-y) in direction[new_grid]:
                            dsu.union(i * column + j,new_x * column + new_y)
        return dsu.find(row * column - 1) == dsu.find(0)
        # (row - 1) * (column - 1) + (column - 1)
        # row*Column -row 
        # row(column - 1)
        r = m
        c = n
        m-1 * c + c-1
        cm - c + c - 1
