class UnionFind:
    def __init__(self):
        self.parent =dict()
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
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = UnionFind()
        for i,j in pairs:
            dsu.union(i,j)
        
        target = defaultdict(list)
        for i in range(len(s)):
            root  = dsu.find(i)
            target[root].append(s[i])
        for i in target:
            target[i].sort(reverse = True)
        res = []
        for i in range(len(s)):
            root  = dsu.find(i)
            letter = target[root].pop()
            res.append(letter)
        print(target)
        print(res)
        return "".join(res)
        