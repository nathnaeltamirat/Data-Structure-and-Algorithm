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
                self.size[rootx] += self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = UnionFind()
        parent  = defaultdict(int)

        for i in range(len(stones)):
            x, y = stones[i]
            for j in range(i+1,len(stones)):
                new_x, new_y = stones[j]
                if new_x == x or new_y == y:
                    dsu.union(i,j)
        for i in range(len(stones)):
            parent[dsu.find(i)] += 1
        res = 0
        for i in parent:
            res += parent[i] - 1
        return res
        print(parent)
            
