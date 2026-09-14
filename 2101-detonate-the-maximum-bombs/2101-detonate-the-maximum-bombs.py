class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited = set()
        res = 1
        def dfs(i):
            x,y,r = bombs[i]
            visited.add(i)
            res = 1
            for j in range(len(bombs)):
                if j != i and j not in visited:
                    new_x,new_y, _ = bombs[j]
                    
                    if( (x-new_x)**2 + (y-new_y)**2 <= r*r):

                        res += dfs(j)
            return res
        for i in range(len(bombs)):
            visited = set()
            res = max(res,dfs(i))
        return res