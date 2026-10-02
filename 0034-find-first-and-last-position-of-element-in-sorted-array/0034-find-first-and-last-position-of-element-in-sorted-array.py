class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lower = bisect_left(nums,target)
        if  lower >= len(nums) or nums[lower] != target:
            return [-1,-1]
        return [lower,bisect_right(nums,target)-1]