from collections import defaultdict
class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(lambda:1)
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootx, rooty = self.find(x), self.find(y)
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = UnionFind()
        holder = defaultdict(list)
        for a,b in pairs:
            dsu.union(a,b)
        for i in range(len(s)):
            holder[dsu.find(i)].append(s[i])
        for item in holder:
            holder[item].sort(reverse = True)
        res = []
        for i in range(len(s)):
            value = holder[dsu.find(i)].pop()
            res.append(value)
        print(res)   
        return "".join(res) 
       