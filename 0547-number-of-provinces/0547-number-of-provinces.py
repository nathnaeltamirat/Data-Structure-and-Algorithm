class UnionFind:
    def __init__(self,size):
        self.parent = {i:i for i in range((size))}
        self.size = [1] * size
    def find(self,x):
        while  self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def CountProvince(self):
        count = set()
        for i in range(len(self.size)):
            count.add(self.find(i))
        print(count)
        return len(count)
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
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] != 0:
                    dsu.union(i,j)
        return dsu.CountProvince()
