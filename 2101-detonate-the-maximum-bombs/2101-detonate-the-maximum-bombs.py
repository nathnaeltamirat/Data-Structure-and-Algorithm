class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = 1

        def dfs(i,visited):
            visited.add(i)
            val = 1
            x,y,r = bombs[i]
            for j in range(len(bombs)):
                if  j!= i and j not in visited:
                    new_x, new_y , _ = bombs[j]
                    dx = new_x - x
                    dy = new_y  - y
                    if (dx * dx) + (dy * dy) <= r * r:
                        val += dfs(j,visited)
            return val

        for i in range(len(bombs)):
                x, y,r = bombs[i]
                res = max(res,dfs(i,set()))
        return res