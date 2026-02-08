class UnionFind:
    def __init__(self,n):
        self.parent = dict()
        self.size = defaultdict(lambda : 1)
        self.connected = n
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
                self.size[rootx] += rooty
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += rootx
            self.connected -= 1
     

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    dsu.union(i,j)
        
        return dsu.connected