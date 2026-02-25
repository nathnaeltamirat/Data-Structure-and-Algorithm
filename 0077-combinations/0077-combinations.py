class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(curr,path):

            if len(path) == k:
                res.append(path[:])
                return
            max_value = n - (k - len(path)) + 2
            for i in range(curr,max_value):
                path.append(i)
                backtrack(i+1,path)
                path.pop()

        backtrack(1,[])
        return res