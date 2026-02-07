class UnionFind:
    def __init__(self,n):
        self.parent = dict()
        self.size = defaultdict(lambda: 1)
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
        edges.sort(reverse = True)
        alice_dsu = UnionFind(n)
        res = 0
        bob_dsu = UnionFind(n)
        for t, a, b in edges:
            if alice_dsu.isConnected(a,b) and bob_dsu.isConnected(a,b):
                res += 1
                continue
            if t == 3:
                alice_dsu.union(a,b)
                bob_dsu.union(a,b)
            elif t == 1:
                if alice_dsu.isConnected(a,b):
                    res += 1
                    continue
                alice_dsu.union(a,b)
            else:
                if bob_dsu.isConnected(a,b):
                    res += 1
                    continue
                bob_dsu.union(a,b)

        if alice_dsu.connected != 1 or bob_dsu.connected != 1:
            return -1
        return res
