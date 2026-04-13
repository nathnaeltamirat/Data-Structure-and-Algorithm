class UnionFind:
    def __init__(self):
        self.root = dict()
        self.size = defaultdict(lambda:1)
    def find(self,x):
        if x not in self.root:
            self.root[x] = x
            return x
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.size[rootx] += self.size[rooty]
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                self.size[rooty] += self.size[rootx] 
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        #flattening formula
 
        dsu = UnionFind()
        dir = {
            1: [(0,-1),(0,1)], #left and right
            2: [(-1,0),(1,0)], #upper and lower
            3: [(0,-1), (1,0)], #left and lower
            4: [(0,1),(1,0)], #right and lower
            5: [(0,-1),(-1,0)], #left and upeer
            6: [(0,1),(-1,0)] #right and upper
        }
        row, column = len(grid), len(grid[0])

        def inBound(r,c):
            return r >= 0 and c >= 0 and r < row and c < column

        for i in range(row):
            for j in range(column):
                val = grid[i][j]
                for x, y in dir[val]:
                    new_r = i + x
                    new_c = j + y
                    if inBound(new_r,new_c):
                        if (-x,-y) in dir[grid[new_r][new_c]]:
                            dsu.union((i * column + j),(new_r * column  + new_c))
        return dsu.find((row -1) * (column) + (column - 1) )== dsu.find(0)