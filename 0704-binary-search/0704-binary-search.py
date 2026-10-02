class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = low + (high - low)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return -1