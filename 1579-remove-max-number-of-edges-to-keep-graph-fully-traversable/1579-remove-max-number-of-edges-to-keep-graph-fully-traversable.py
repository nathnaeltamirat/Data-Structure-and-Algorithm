class UnionFind:
    def __init__(self):
        self.root = dict()
        self.size = defaultdict(lambda:1)
    def find(self,x):
        if x not in self.root:
            self.root[x] = x
            return x
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.root[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.root[rootx] = rooty
                self.size[rooty] += self.size[rootx]
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind()
        bob = UnionFind()
     
        res = 0
        #1 alice
        #2 bob
        for t, a, b in edges:
            if t == 3:
                if alice.isConnected(a,b) and bob.isConnected(a,b):
                    res += 1
                else:
                    alice.union(a,b)
                    bob.union(a,b)
        for t, a, b in edges:
            if t == 2:
                if bob.isConnected(a,b):
                    res += 1
                else:
                    bob.union(a,b)
            elif t == 1:
                if alice.isConnected(a,b):
                    res += 1
                else:
                    alice.union(a,b)
        for i in range(1,n+1):
            if not alice.isConnected(1,i):
                return -1
            if not bob.isConnected(1,i):
                return -1
        return res 