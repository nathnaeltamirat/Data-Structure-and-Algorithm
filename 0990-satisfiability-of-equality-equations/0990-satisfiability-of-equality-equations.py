class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(lambda : 1)
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
            return True
      
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = UnionFind()
        for equation in equations:
            first, o1,o2,second = equation
            op = o1 + o2
            if op == "==":
                dsu.union(first,second)
        for equation in equations:
            first, o1,o2,second = equation
            op = o1 + o2
            if op == "!=":
                if dsu.find(first) == dsu.find(second):
                    return False
        return True