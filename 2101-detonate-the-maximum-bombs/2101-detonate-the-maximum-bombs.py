class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited = set()
        def dfs(i):
            count = 1
            x,y,r = bombs[i]
            if i == 1:
                print(x,y,r)
            for j in range(len(bombs)):
                if i == 1:
                    print(j)
                if j == i or j in visited:
                    continue
                
                new_x, new_y, _ = bombs[j]
                if i == 1:
                    print(x,y,new_x,new_y)
                    
                # print(x,y,new_x,new_y)
                if (new_x - x) **2 + (new_y - y)**2 <= r**2:
                    visited.add(j)
                    count += dfs(j)
            return count
        res = 1
        for i in range(len(bombs)):
       
            visited = set()
            visited.add(i)
            res = max(res,dfs(i))
        
        return res
                
