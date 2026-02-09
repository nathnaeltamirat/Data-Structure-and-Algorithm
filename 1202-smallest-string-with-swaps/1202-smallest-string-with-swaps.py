class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(lambda: 1)
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if self.parent[x] == x:
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
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        sorter = defaultdict(list)
        dsu = UnionFind()

        for i, (a,b) in enumerate(pairs):
            dsu.union(a,b)
        for i in range(len(s)):
            root = dsu.find(i)
            sorter[root].append(s[i])
        for i in sorter:
            sorter[i].sort(reverse = True)
        res = []
        for i in range(len(s)):
            root = dsu.find(i)
            res.append(sorter[root].pop())
        print(res)
        return "".join(res)