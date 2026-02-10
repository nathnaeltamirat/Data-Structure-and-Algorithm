class UnionFind:
    def __init__(self,n):
        self.parent = dict()
        self.size = defaultdict(lambda:1)
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
                self.size[rootx] += self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            self.connected-=1
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu_alice = UnionFind(n)
        dsu_bob = UnionFind(n)
        edges.sort(reverse = True)
        res = 0
        for i in range(len(edges)):
            t,a,b = edges[i]
            if t == 3:
                if dsu_alice.isConnected(a,b) and  dsu_bob.isConnected(a,b):
                    res += 1
                else:
                    dsu_alice.union(a,b)
                    dsu_bob.union(a,b)
            elif t == 2:
                if dsu_bob.isConnected(a,b):
                    res += 1
                else:
                    dsu_bob.union(a,b)
            else:
                if dsu_alice.isConnected(a,b):
                    res += 1
                else:
                    dsu_alice.union(a,b)

        if dsu_alice.connected != 1 or dsu_bob.connected != 1:
            return -1
        return res