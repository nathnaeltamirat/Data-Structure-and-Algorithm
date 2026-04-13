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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = UnionFind()
        edgeList.sort(key = lambda x: x[2])
        queries = sorted((val,a,b,idx) for idx,(a,b,val) in enumerate(queries))
        ans = [0] * len(queries)
        curr_e = 0
        for i in range(len(queries)):
            while not dsu.isConnected(queries[i][1],queries[i][2]) and curr_e < len(edgeList) and edgeList[curr_e][2] < queries[i][0]:
                dsu.union(edgeList[curr_e][0],edgeList[curr_e][1])
                curr_e += 1
            ans[queries[i][3]] = dsu.isConnected(queries[i][1],queries[i][2])
        return ans


