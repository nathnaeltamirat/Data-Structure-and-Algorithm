class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited = set()
       
        def dfs(i):
            visited.add(i)
            count = 1
            x, y,r = bombs[i]
            for j in range(len(bombs)):
                if i != j and  j not in visited:
                    n_x, n_y, _ = bombs[j]
                    if((x-n_x)**2 + (y-n_y)**2 <=r*r):
                        count += dfs(j)
            
            return count
        res = 1
        for i in range(len(bombs)):
            visited = set()
            res = max(res,dfs(i))
        return res