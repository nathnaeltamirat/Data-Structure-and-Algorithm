class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        low = 0
        high = max(nums) - min(nums)
        nums.sort()
        def counter(medium):
            count = 0
            for i in range(len(nums)):
                right = bisect_right(nums,nums[i] + medium,i+1)
                count += right - (i + 1)
            return count
        while low < high:
            medium = low + (high - low)//2
            if counter(medium) >= k:
                high = medium
            else:
                low = medium + 1
        return low
