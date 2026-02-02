class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

        res = 1
        def dfs(i,visited):
            visited.add(i)
            x, y, r = bombs[i]
            ans = 1
            for j in range(len(bombs)):
                if j not in visited:
                    new_x, new_y, new_r = bombs[j]
                    dx = new_x - x
                    dy = new_y - y
                    if (dx * dx) + (dy * dy) <= r * r:
   
                        ans += dfs(j,visited)
            return ans
        for i in range(len(bombs)):
            val = dfs(i,set())
            print(val,i)
            res = max(res,dfs(i,set()))

        return res