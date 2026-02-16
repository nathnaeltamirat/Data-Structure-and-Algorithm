class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookie = [0] * k
        self.res = float('inf')
        def backtrack(i,max_so_far):
            if max_so_far > self.res:
                return
            if i >= len(cookies):
                self.res = min(self.res,max_so_far)
                return
            for j in range(k):
                cookie[j] += cookies[i]
                backtrack(i+1,max(max_so_far,cookie[j]))
                cookie[j] -= cookies[i]
                if cookie[j] == 0:
                    break
        backtrack(0,0)
        return self.res
            