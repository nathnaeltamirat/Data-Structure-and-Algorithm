class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        left = right = nums[0][0]
        min_heap = []
        for i in range(len(nums)):
            num = nums[i][0]
            left = min(left,num)
            right = max(right,num)
            heappush(min_heap,(num,i,0))
        res = [left,right]
        while True:
            num, list_idx, idx = heappop(min_heap)
            idx += 1
            if idx == len(nums[list_idx]):
                return res
            
            next_val = nums[list_idx][idx]
            heappush(min_heap,(next_val,list_idx,idx))
            right = max(right,next_val)
            left = min_heap[0][0]
            if right -left < res[1] - res[0]:
                res = [left,right]