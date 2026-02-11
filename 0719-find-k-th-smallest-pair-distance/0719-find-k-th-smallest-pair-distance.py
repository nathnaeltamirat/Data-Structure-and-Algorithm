class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def kGiver(d):
            count = 0
            for i in range(len(nums)):
                diff = nums[i] + d
                val = bisect_right(nums,diff,i+1) - 1 - i
                count += val
            return count

        low = 0
        high = max(nums) - min(nums)
        while low < high:
            middle = low + (high - low)//2
            if kGiver(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low