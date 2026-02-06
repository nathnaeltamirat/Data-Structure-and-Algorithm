class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(lambda:1)
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
        if  rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
            return []
        else:
            return [x,y]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        dsu = UnionFind()
        for a, b in edges:
            val = dsu.union(a,b)
            if val:
                res.append(val)
        print(res)
        return res[-1]
