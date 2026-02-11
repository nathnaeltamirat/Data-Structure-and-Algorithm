class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        for i in range(0,k):
            window_sum += nums[i]
        res = window_sum/k
        for i in range(k,len(nums)):
            window_sum -= nums[i - k]
            window_sum += nums[i]
            average = window_sum/k
            res = max(average,res)
        return res