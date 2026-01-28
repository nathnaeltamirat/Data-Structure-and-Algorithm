class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = float('inf')
        while low <= high:
            middle = low + (high - low)//2
            if nums[middle] > nums[high]:
                low = middle + 1
            elif nums[middle] < nums[high]:
                high = middle
            else:
                high -=1
            res = min(res,nums[middle])
        return res