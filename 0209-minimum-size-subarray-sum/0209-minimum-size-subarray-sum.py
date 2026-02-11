class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        summation = 0
        for r in range(len(nums)):
            summation += nums[r]
            while summation >= target:
                res = min(res,r-l+1)
                summation -= nums[l]
                l+=1
        return res if res != float('inf') else 0