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
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.parent[rooty] = rootx
                self.size[rootx]+= self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = UnionFind()
        idx_with_queries = [ [idx,a,b,dist] for idx, (a,b,dist) in enumerate(queries)]
        edgeList.sort(key = lambda x: x[2])
        idx_with_queries.sort(key = lambda x: x[3]) 
        res = [0] * len(queries)


        e = 0
        for idx,a,b,dist in idx_with_queries:
            while e < len(edgeList) and  edgeList[e][2] < dist:
                dsu.union(edgeList[e][0],edgeList[e][1])
                e+=1
            res[idx] = dsu.isConnected(a,b)
        return res
             
