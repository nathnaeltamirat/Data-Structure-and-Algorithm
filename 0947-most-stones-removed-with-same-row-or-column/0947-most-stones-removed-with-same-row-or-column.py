class UnionFind:
    def __init__(self,n):
        self.parent = dict()
        self.size = defaultdict(lambda:1)
        self.isConnected = n
    
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
            self.isConnected-=1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        dsu = UnionFind(n)
        row = {}
        col = {}
        
        for i in range(len(stones)):
            x,y = stones[i]
            if x in row:
                dsu.union(row[x],i)
            else:
                row[x] = i
            if y in col:
                dsu.union(col[y],i)
            else:
                col[y] = i

        return n - dsu.isConnected
            
