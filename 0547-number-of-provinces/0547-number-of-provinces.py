class UnionFind:
    def __init__(self,n):
        self.apart = n
        self.size = defaultdict(lambda:1)
        self.root = dict()
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
                self.root[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.root[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            self.apart-=1
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    dsu.union(i,j)
        
        return dsu.apart