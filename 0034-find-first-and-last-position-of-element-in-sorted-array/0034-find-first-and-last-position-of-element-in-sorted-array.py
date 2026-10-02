class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1
        res = [-1,-1]
        while low <= high:
            middle = low + (high - low)//2
            if nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1
            else:
                res[0] = middle
                high = middle - 1

        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = low + (high - low)//2
            if nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:     
                low = middle + 1
            else:
                low = middle + 1
                res[1] = middle


        return res