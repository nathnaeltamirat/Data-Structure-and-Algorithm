class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        res = float('inf')
        q = deque()
        summation = 0
        min_heap = []
        for r in range(len(nums)):
            summation += nums[r]
            if summation >= k:
                res = min(res,r+1)
            
            while q and summation < q[-1][0]:
                q.pop()
            
            while q and  summation - q[0][0] >= k:
                prefix,idx = q.popleft()
                res = min(res,r-idx)
            
            q.append((summation,r))


        return res if res != float('inf') else -1