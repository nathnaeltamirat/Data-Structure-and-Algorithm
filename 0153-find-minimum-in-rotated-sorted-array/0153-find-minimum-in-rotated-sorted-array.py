class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = 0
        while low < high:
            middle = low + (high - low)//2
            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle
        return nums[low]

