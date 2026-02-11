class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        res = float('inf')
        summation = 0
        min_heap = []
        for r in range(len(nums)):
            summation += nums[r]
            if summation >= k:
                res = min(res,r-l+1)
            while min_heap and  summation - min_heap[0][0] >= k:
                prefix,idx = heappop(min_heap)
                res = min(res,r-idx)
            heappush(min_heap,(summation,r))
        return res if res != float('inf') else -1