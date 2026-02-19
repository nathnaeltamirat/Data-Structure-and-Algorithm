class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify_max(nums)
        for i in range(k):
            if i == k -1:
                return heappop_max(nums)
            heappop_max(nums)