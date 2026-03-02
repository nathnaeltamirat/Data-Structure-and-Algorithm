class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        visited = set()
        def dfs(i):
            count = 1
            visited.add(i)
            x,y,r = bombs[i]
            for j in range(len(bombs)):
                if i == j or j in visited:
                    continue
                
                new_x, new_y, _ = bombs[j]
                if (new_x - x)** 2 + (new_y - y) ** 2 <= r*r:
                    count += dfs(j)
                    visited.add(j)
            return count
        res = 1
        for i in range(len(bombs)):
            visited = set()
            res = max(res,dfs(i))
        
        return res



  