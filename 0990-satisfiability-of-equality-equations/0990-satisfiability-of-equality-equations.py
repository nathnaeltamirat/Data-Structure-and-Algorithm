class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(lambda:1)
    def find(self,x):
        if x not in self.parent:
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
                self.size[rootx] += self.size[rooty]
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = UnionFind()
        disUnion = []
        for equation in equations:
            a, o,p, b = equation
            op = o + p
            a = ord(a) - ord('a') 
            b = ord(b) - ord('a')
            if op == "!=":
                disUnion.append((a,b))
                continue
            dsu.union(a,b)
        for a,b in disUnion:
            if dsu.isConnected(a,b):
                return False
        return True
