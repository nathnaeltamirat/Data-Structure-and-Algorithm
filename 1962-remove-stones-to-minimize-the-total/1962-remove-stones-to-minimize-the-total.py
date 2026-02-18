class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heapify_max(piles)
        res = 0
        i = 0
        while i < k:
            max_value =  heappop_max(piles)
            taken = floor(max_value/2)
            heappush_max(piles,max_value - taken)
            i+=1
        return sum(piles)