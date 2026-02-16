class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #1 --- 4
         # 2 ---- 4
        res = []
        def backtrack(curr,path):
            nonlocal res
            if len(path) == k:
                print(path)
                res.append(path[:])
                return
            for i in range(curr, n+1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        backtrack(1,[])
        return res